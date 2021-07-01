from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_order_global_discount = fields.Boolean(
        string="A Income Tax on invoices/bills",
        implied_group='discount_account_invoice.group_order_global_discount',
        config_parameter='account.group_order_global_discount',
        help="Allows to give a Income Tax on invoice/bills. ")
    global_discount_tax = fields.Selection(
        selection=[('untax', 'Untaxed amount'), ('taxed', 'Tax added amount')],
        string="Income Tax Calculation",
        default="untax",
        help="Income Tax calculation will be ( \
             'untax' : Income Tax will be applied before applying tax, \
             'taxed : Income Tax will be applied after applying tax)")
    discount_account_invoice = fields.Many2one(
        string="Income Tax Account",
        comodel_name='account.account',
        related="company_id.discount_account_invoice",
        readonly=False,
        help="Account for Global discount on invoices.")
    discount_account_bill = fields.Many2one(
        string="Income Tax",
        comodel_name='account.account',
        related="company_id.discount_account_bill",
        readonly=False,
        help="Account for Income Tax on bills.")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrConfigPrmtr = self.env['ir.config_parameter'].sudo()
        IrConfigPrmtr.set_param('account.group_order_global_discount',
                                self.group_order_global_discount)
        IrConfigPrmtr.set_param('account.global_discount_tax',
                                self.global_discount_tax)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrConfigPrmtr = self.env['ir.config_parameter'].sudo()
        group_order_global_discount = IrConfigPrmtr.get_param(
            'account.group_order_global_discount')
        global_discount_tax = IrConfigPrmtr.get_param(
            'account.global_discount_tax')
        res.update({
            'group_order_global_discount': group_order_global_discount,
            'global_discount_tax': global_discount_tax,
        })
        return res
