# -*- coding: utf-8 -*-

from odoo import models


class HrPayslipInh(models.Model):
    _inherit = 'hr.payslip'

    def _action_create_account_move(self):
        record = super(HrPayslipInh, self)._action_create_account_move()
        for rec in self:
            for line in rec.move_id.line_ids:
                line.partner_id = rec.employee_id.address_home_id.id
        return record
