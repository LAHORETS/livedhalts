# -*- coding: utf-8 -*-

from odoo import models, api, fields, models, _
from odoo.tools import float_compare, float_is_zero
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        record = super(PurchaseOrderInherit, self).button_confirm()
        for rec in self.picking_ids:
            rec.scheduled_date = self.date_order


class AccountMoveInh(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        if self.type == 'entry':
            slip = self.env['hr.payslip'].search([('number', '=', self.ref)])
            if slip:
                slip.loan_line.status = 'paid'
                slip.loan_line.paid = True
                slip.loan_line.paid_on = datetime.today()
                slip.loan_line.paid_amount = slip.loan_line.amount
        return super(AccountMoveInh, self).action_post()


class HrAdvanceInh(models.Model):
    _inherit = 'hr.advance'

    journal_id = fields.Many2one('account.journal')
    is_payment_created = fields.Boolean('Is Created', default=False)
    move_id = fields.Many2one('account.move')

    def action_view_entry(self):
        return {
            'type': 'ir.actions.act_window',
            'binding_type': 'object',
            'domain': [('ref', '=', self.name)],
            'target': 'current',
            'name': 'Journal Item',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
        }

    def action_create_payment(self):
        self._action_general_entry()

    def _action_general_entry(self):
        line_ids = []
        debit_sum = 0.0
        credit_sum = 0.0
        for rec in self:
            if not rec.journal_id:
                raise UserError('Please Select Journal.')
            debit_account = self.env['account.account'].search([('name', '=', 'Advances to Employees against Salary')])
            if not debit_account:
                raise UserError('Debit Account not Found.')
            move_dict = {
                'ref': rec.name,
                'journal_id': rec.journal_id.id,
                'partner_id': rec.employee_id.address_home_id.id,
                'date': datetime.today(),
                'state': 'draft',
            }
            debit_line = (0, 0, {
                'name': 'Advances to Employees against Salary',
                'debit': abs(rec.loan_amount),
                'credit': 0.0,
                'partner_id': rec.employee_id.address_home_id.id,
                'account_id': debit_account.id,
            })
            line_ids.append(debit_line)
            debit_sum += debit_line[2]['debit'] - debit_line[2]['credit']
            credit_line = (0, 0, {
                'name': 'Advances to Employees against Salary',
                'debit': 0.0,
                'partner_id': rec.employee_id.address_home_id.id,
                'credit': abs(rec.loan_amount),
                'account_id': rec.journal_id.default_credit_account_id.id,
            })
            line_ids.append(credit_line)
            credit_sum += credit_line[2]['credit'] - credit_line[2]['debit']

            move_dict['line_ids'] = line_ids
            move = self.env['account.move'].create(move_dict)
            line_ids = []
            rec.is_payment_created = True
            rec.move_id = move.id
            print("General entry created")


class HrAdvanceLineInh(models.Model):
    _inherit = 'hr.advance.line'

    paid_on = fields.Date()
    paid_amount = fields.Float()
    status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ], string="Status", default='unpaid', copy=False )


class HrLoanInh(models.Model):
    _inherit = 'hr.loan'

    journal_id = fields.Many2one('account.journal')
    is_payment_created = fields.Boolean('Is Created', default=False)
    move_id = fields.Many2one('account.move')

    def action_view_entry(self):
        return {
            'type': 'ir.actions.act_window',
            'binding_type': 'object',
            'domain': [('ref', '=', self.name)],
            'target': 'current',
            'name': 'Journal Item',
            'res_model': 'account.move',
            'view_mode': 'tree,form',
        }

    def action_create_payment(self):
        self._action_general_entry()

    def _action_general_entry(self):
        line_ids = []
        debit_sum = 0.0
        credit_sum = 0.0
        for rec in self:
            if not rec.journal_id:
                raise UserError('Please Select Journal.')
            debit_account = self.env['account.account'].search([('name', '=', 'Loan against PF')])
            move_dict = {
                'ref': rec.name,
                'journal_id': rec.journal_id.id,
                'partner_id': rec.employee_id.address_home_id.id,
                'date': datetime.today(),
                'state': 'draft',
            }
            debit_line = (0, 0, {
                'name': 'Loan Against PF',
                'debit': abs(rec.loan_amount),
                'credit': 0.0,
                'partner_id': rec.employee_id.address_home_id.id,
                'account_id': debit_account.id,
            })
            line_ids.append(debit_line)
            debit_sum += debit_line[2]['debit'] - debit_line[2]['credit']
            credit_line = (0, 0, {
                'name': 'Loan Against PF',
                'debit': 0.0,
                'partner_id': rec.employee_id.address_home_id.id,
                'credit': abs(rec.loan_amount),
                'account_id': rec.journal_id.default_credit_account_id.id,
            })
            line_ids.append(credit_line)
            credit_sum += credit_line[2]['credit'] - credit_line[2]['debit']

            move_dict['line_ids'] = line_ids
            move = self.env['account.move'].create(move_dict)
            line_ids = []
            rec.is_payment_created = True
            rec.move_id = move.id
            print("General entry created")


class HrLoanLineInh(models.Model):
    _inherit = 'hr.loan.line'

    paid_on = fields.Date()
    paid_amount = fields.Float()
    status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
    ], string="Status", default='unpaid', copy=False )


class HrEmployeeInh(models.Model):
    _inherit = 'hr.employee'

    employer_cont = fields.Float()
    employee_cont = fields.Float()

    @api.model
    def create(self, vals):
        rec = super(HrEmployeeInh, self).create(vals)
        record = self.env['res.partner'].create({
            'name': vals['name'],
        })
        rec.address_home_id = record
        return rec


class HrPayslipInh(models.Model):
    _inherit = 'hr.payslip'

    loan_amount = fields.Float()
    advance_amount = fields.Float()
    loan_line = fields.Many2one('hr.loan.line')
    advance_line = fields.Many2one('hr.advance.line')

    def compute_sheet(self):
        for rec in self:
            # Loans
            loan = self.env['hr.loan'].search([('employee_id', '=', rec.employee_id.id), ('state', '=', 'approve'), ('is_payment_created', '=', True)])
            amount = 0
            if loan and loan.move_id.state == 'posted':
                for line in loan.loan_lines:
                    if rec.date_from.month == line.date.month and line.status != 'paid':
                        amount = amount + line.amount
                        rec.loan_line = line.id
            rec.loan_amount = amount

            # Advances
            loan = self.env['hr.advance'].search([('employee_id', '=', rec.employee_id.id), ('state', '=', 'approve'),
                                               ('is_payment_created', '=', True)])
            ad_amount = 0
            if loan and loan.move_id.state == 'posted':
                for line in loan.advance_lines:
                    if rec.date_from.month == line.date.month and line.status != 'paid':
                        ad_amount = ad_amount + line.amount
                        rec.advance_line = line.id
            rec.advance_amount = ad_amount

            return super(HrPayslipInh, self).compute_sheet()

    def action_payslip_done(self):
        record = super(HrPayslipInh, self).action_payslip_done()
        self._action_general_entry()

    def _action_general_entry(self):
        line_ids = []
        debit_sum = 0.0
        credit_sum = 0.0
        for rec in self:
            move_dict = {
                'ref': rec.number,
                'journal_id': rec.journal_id.id,
                'partner_id': rec.employee_id.address_home_id.id,
                'date': datetime.today(),
                'state': 'draft',
            }
            for oline in rec.line_ids:
                if oline.salary_rule_id.account_debit and oline.salary_rule_id.account_credit and oline.total > 0:
                    if oline.code == 'EC':
                        # rec.employee_id.employee_cont = rec.employee_id.employee_cont + oline.total
                        rec.employee_id.employer_cont = rec.employee_id.employer_cont + oline.total
                    if oline.code == 'PF':
                        rec.employee_id.employee_cont = rec.employee_id.employee_cont + oline.total
                        # rec.employee_id.employer_cont = rec.employee_id.employer_cont + oline.total
                    debit_line = (0, 0, {
                        'name': oline.name,
                        'debit': abs(oline.total),
                        'credit': 0.0,
                        'partner_id': oline.slip_id.employee_id.address_home_id.id,
                        'account_id': oline.salary_rule_id.account_debit.id,
                    })
                    line_ids.append(debit_line)
                    debit_sum += debit_line[2]['debit'] - debit_line[2]['credit']
                    credit_line = (0, 0, {
                        'name': oline.name,
                        'debit': 0.0,
                        'partner_id': oline.slip_id.employee_id.address_home_id.id,
                        'credit': abs(oline.total),
                        'account_id': oline.salary_rule_id.account_credit.id,
                    })
                    line_ids.append(credit_line)
                    credit_sum += credit_line[2]['credit'] - credit_line[2]['debit']
            if line_ids:
                move_dict['line_ids'] = line_ids
                move = self.env['account.move'].create(move_dict)
                line_ids = []
                rec.move_id = move.id
                print("General entry created")
