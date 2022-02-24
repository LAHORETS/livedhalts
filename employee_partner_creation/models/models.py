# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployeeInh(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        rec = super(HrEmployeeInh, self).create(vals)
        record = self.env['res.partner'].create({
            'name': vals['name'],
        })
        rec.address_home_id = record
        return rec

