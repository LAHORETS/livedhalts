# -*- coding: utf-8 -*-


import datetime
from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    state = fields.Selection([
        ('draft', 'RFQ'),
        ('sent', 'RFQ Sent'),
        ('manager_approve', 'Waiting For Manager Approval'),
        ('cfo_approve', 'Waiting For CFO Approval'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('reject', 'Rejected'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    def button_confirm(self):
        if self.amount_total < 100000:
            self.write({
                'state': 'manager_approve'
            })
        elif self.amount_total >= 100000:
            self.write({
                'state': 'cfo_approve'
            })

    def button_manager_approve(self):
        for order in self:
            if order.state not in ['draft', 'sent','manager_approve']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step'\
                    or (order.company_id.po_double_validation == 'two_step'\
                        and order.amount_total < self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today()))\
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
        return True

    def button_cfo_approved(self):
        for order in self:
            if order.state not in ['draft', 'sent','cfo_approve']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step'\
                    or (order.company_id.po_double_validation == 'two_step'\
                        and order.amount_total < self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today()))\
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
        return True

    def button_manager_reject(self):
        self.write({
            'state': 'reject'
        })

    def button_cfo_reject(self):
        self.write({
            'state': 'reject'
        })


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('manager_approve', 'Waiting For Manager Approval'),
        ('cfo_approve', 'Waiting For CFO Approval'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled'),
        ('reject', 'Rejected'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')

    def action_post(self):
        if self.amount_total < 100000:
            self.write({
                'state': 'manager_approve'
            })
        elif self.amount_total >= 100000:
            self.write({
                'state': 'cfo_approve'
            })

    def button_manager_approve(self):
        res = super(AccountMoveInherit, self).action_post()
        return res

    def button_cfo_approved(self):
        res = super(AccountMoveInherit, self).action_post()
        return res

    def button_manager_reject(self):
        self.write({
            'state': 'reject'
        })

    def button_cfo_reject(self):
        self.write({
            'state': 'reject'
        })


class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'

    def action_post(self):
        if self.amount < 100000:
            self.write({
                'state': 'manager_approve'
            })
        elif self.amount >= 100000:
            self.write({
                'state': 'cfo_approve'
            })

    def button_manager_approve(self):
        res = super(AccountPaymentInherit, self).action_post()
        return res

    def button_cfo_approved(self):
        res = super(AccountPaymentInherit, self).action_post()
        return res

    def button_manager_reject(self):
        self.write({
            'state': 'reject'
        })

    def button_cfo_reject(self):
        self.write({
            'state': 'reject'
        })
