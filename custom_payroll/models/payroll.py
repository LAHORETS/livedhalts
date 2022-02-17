# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrContractInherit(models.Model):
    _inherit = 'hr.contract'

    fuel_allowance = fields.Float(string="Fuel Allowance")
    mobile_allowance = fields.Float(string="Mobile Allowance")
    meal_allowance = fields.Float(string="Meal Allowance")
    arears = fields.Float(string="Arears / Reimbursement")
    car_allowance = fields.Float(string="Car Monetization  Allowance")
    driver_allowance = fields.Float(string="Driver Allowance")
    over_time = fields.Float(string="Over Time")
    other_allowance = fields.Float(string="Other Allowance")

    income_tax = fields.Float(string="Income Tax")
    advances = fields.Float(string="Advances / Loans")
    provident_fund = fields.Float(string="Provident Fund")
    unpaid_leaves = fields.Float(string="Absents / Leaves Without Pay")
    other_deductions = fields.Float(string="Other Deductions")


class HrPayslipInherit(models.Model):
    _inherit = 'hr.payslip'

    unpaid_leave = fields.Float(string="Leaves Without Pay")

