# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WithHoldingText(models.Model):
    _name = 'wth.tax'
    _description = 'With Holding Tax'
    _rec_name = 'wh_tax'

    wh_tax = fields.Char('Withholding Tax', required=1)
    text_scope = fields.Selection(
        [('customer_payment', 'Customer Payment'),
         ('vendor_payment', 'Vendor Payment')],
        string='Tax Scope',
        default='customer_payment'
    )

    tax_computation = fields.Selection(
        [('percentage_price', 'Percentage of Price'),
         # ('group_taxes', 'Group of Taxes'),
         ('fixed', 'Fixed'),
         # ('fixed', 'Fixed'),
         # ('per_price_tax_inc', 'Percentage of Price Tax Included'),
         # ('etc', 'ETC')
         ],
        string='Tax Computation',
        default='percentage_price'
    )
    amount = fields.Float('Amount')
    account_id = fields.Many2one('account.account', 'Withholding Income Tax')
    payment_excess = fields.Float('Payment in excess of')
    # Advance options
    label_on_invoice = fields.Char('Label on Invoice')
    tax_group_id = fields.Many2one('account.tax.group', string="Tax Group")
    tags = fields.Char('Tags')
    inc_analytic_cost = fields.Boolean('Include in Analytic Cost')

    base_amount_calc = fields.Selection(
        [('net_amount', 'Net Amount'),
         ('gross_amount', 'Gross Amount'),
         ('tax_amount', 'Tax Amount')],
        string='Base Amount Calculation',
    )

    control_amount_calc = fields.Selection(
        [('manual_base_amount', 'Manual Base Amount'),
         ('manual_tax_amount', 'Manual Tax Amount'),
         ('none', 'None')],
        string='Control Amount Calculation', default='none'
    )


class WthLines(models.Model):
    _name = 'wth.lines'

    wht_id = fields.Many2one('wth.tax', 'Withholding Tax Code')
    base_amount = fields.Float('Base Amount')
    tax_amount = fields.Float('Tax Amount')
    account_move_id = fields.Many2one('account.move', 'Account')
    account_payment_id = fields.Many2one('account.payment', 'Account')
    untaxed_amount = fields.Float()
    sales_tax = fields.Float()
    total_amount = fields.Float()
    percentage = fields.Float(related='wht_id.amount')

    @api.onchange('base_amount', 'wht_id')
    def compute_tax_amount(self):
        for rec in self:
            if rec.wht_id.tax_computation == 'percentage_price':
                rec.tax_amount = rec.base_amount * (rec.percentage/100)