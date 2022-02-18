# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def get_basic(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'BASIC':
                val = line.total
        return val

    def get_hral(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'HRAL':
                val = line.total
        return val

    def get_utal(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'UTAL':
                val = line.total
        return val

    def get_fuel(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'FUEL':
                val = line.total
        return val

    def get_car(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'CAR':
                val = line.total
        return val

    def get_driver(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'DRIVER':
                val = line.total
        return val

    def get_meal(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'MEAL':
                val = line.total
        return val

    def get_overtime(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'OVERTIME':
                val = line.total
        return val

    def get_arears(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'AREARS':
                val = line.total
        return val

    def get_otheral(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'OTHERAL':
                val = line.total
        return val

    def get_bonus(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'BONUS':
                val = line.total
        return val

    def get_pfund(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'PFUND':
                val = line.total
        return val

    def get_incometax(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'INCOMETAX':
                val = line.total
        return val

    def get_eobi(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'EOBI':
                val = line.total
        return val

    def get_pessi(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'PESSI':
                val = line.total
        return val

    def get_loan(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'LOAN':
                val = line.total
        return val

    def get_lwop(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'LWOP':
                val = line.total
        return val

    def get_otherded(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'OTHERDED':
                val = line.total
        return val

    def get_gross(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'GROSS':
                val = line.total
        return val

    def get_net(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'NET':
                val = line.total
        return val

    def get_deductions(self):
        val = 0
        for line in self.line_ids:
            if line.category_id.code == 'DED':
                val = line.total
        return val

    def get_amount_in_words(self):
        val = 0
        for line in self.line_ids:
            if line.code == 'NET':
                val = line.total
        text = self.currency_id.amount_to_text(val)
        return text.title()

    def get_total_salary(self):
        total = self.get_basic() + self.get_hral() + self.get_utal()
        return total

