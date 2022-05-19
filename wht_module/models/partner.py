from odoo import models, fields, api


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    tax_liable = fields.Boolean('Tax Liable')
    wht_ids = fields.Many2many('wth.tax')
    tax_exempt = fields.Boolean('Tax Exempt')
