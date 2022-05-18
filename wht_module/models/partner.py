from odoo import models, fields, api


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    tax_liable = fields.Boolean('Tax Liable')
    wht_id = fields.Many2one('wth.tax', 'Withholding Tax Code')
    tax_exempt = fields.Boolean('Tax Exempt')
