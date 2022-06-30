# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import odoo.addons.decimal_precision as dp

class SaleEstimatelineJob(models.Model):
    _name = "sale.estimate.line.job"
    
    @api.depends('price_unit','product_uom_qty','discount')
    def _compute_amount(self):
        for rec in self:
            if rec.discount:
                disc_amount = (rec.price_unit * rec.product_uom_qty) * rec.discount / 100
                rec.price_subtotal = (rec.price_unit * rec.product_uom_qty) - disc_amount
            else:
                rec.price_subtotal = rec.price_unit * rec.product_uom_qty
            
    estimate_id = fields.Many2one(
        'sale.estimate.job',
        string='Sale Estimate', 
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )
    product_uom_qty = fields.Float(
        string='Quantity', 
        digits=dp.get_precision('Product Unit of Measure'), 
        required=True, 
        default=1.0
    )
    product_uom = fields.Many2one(
        'uom.uom', #produtc.uom
        string='Unit of Measure', 
        required=True
    )
    price_unit = fields.Float(
        'Unit Price', 
        required=True, 
        digits=dp.get_precision('Product Price'), 
        default=0.0
    )
    price_subtotal = fields.Float(
        compute='_compute_amount', 
        string='Subtotal', 
        store=True
    )
    product_description = fields.Char(
        string='Description'
    )
    discount = fields.Float(
        string='Discount (%)'
    )
    company_id = fields.Many2one(related='estimate_id.company_id', string='Company', store=True, readonly=True)
    tax_id = fields.Many2many('account.tax', string='Taxes', domain=['|', ('active', '=', False), ('active', '=', True)])

    job_type = fields.Selection(
        selection=[('material','Material'),
                    ('labour','Labour'),
                    ('overhead','Overhead')
                ],
        string="Type",
        required=True,
    )
    analytic_id = fields.Many2one(
        'account.analytic.account',
        'Analytic Account',
        store=True,
    )

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        if not self.product_id:
            return {'domain': {'product_uom': []}}

        vals = {}
        domain = {'product_uom': [('category_id', '=', self.product_id.uom_id.category_id.id)]}
        if not self.product_uom or (self.product_id.uom_id.id != self.product_uom.id):
            vals['product_uom'] = self.product_id.uom_id
            vals['product_uom_qty'] = 1.0

        product = self.product_id.with_context(
            lang=self.estimate_id.partner_id.lang,
            partner=self.estimate_id.partner_id.id,
            quantity=vals.get('product_uom_qty') or self.product_uom_qty,
            date=self.estimate_id.estimate_date,
            pricelist=self.estimate_id.pricelist_id.id,
            uom=self.product_uom.id
        )

        name = product.name_get()[0][1]
        if product.description_sale:
            name += '\n' + product.description_sale
        vals['product_description'] = name

        self._compute_tax_id()

        if self.estimate_id.pricelist_id and self.estimate_id.partner_id:
            vals['price_unit'] = self.env['account.tax']._fix_tax_included_price(self._get_display_price(product), product.taxes_id, self.tax_id)
        self.update(vals)

        title = False
        message = False
        warning = {}
        if product.sale_line_warn != 'no-message':
            title = _("Warning for %s") % product.name
            message = product.sale_line_warn_msg
            warning['title'] = title
            warning['message'] = message
            if product.sale_line_warn == 'block':
                self.product_id = False
            return {'warning': warning}
        return {'domain': domain}

    @api.multi
    def _compute_tax_id(self):
        for line in self:
            fpos = line.estimate_id.partner_id.property_account_position_id
            # If company_id is set, always filter taxes by the company
            taxes = line.product_id.taxes_id.filtered(lambda r: not line.company_id or r.company_id == line.company_id)
            line.tax_id = fpos.map_tax(taxes, line.product_id, line.estimate_id.partner_id) if fpos else taxes
            
    
    @api.multi
    def _get_display_price(self, product):
        if self.estimate_id.pricelist_id.discount_policy == 'without_discount':
            from_currency = self.estimate_id.company_id.currency_id
            return from_currency.compute(product.lst_price, self.estimate_id.pricelist_id.currency_id)
        return product.with_context(pricelist=self.estimate_id.pricelist_id.id).price
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
