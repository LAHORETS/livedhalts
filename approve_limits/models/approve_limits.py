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
        ('to_review', 'Waiting For Review Approval'),
        ('tax_review', 'Waiting For Tax Review Approval'),
        ('cfo_approve', 'Waiting For Approval'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('reject', 'Rejected'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    def button_confirm(self):
        if self.amount_tax > 0:
            self.write({
                'state': 'tax_review'
            })
        elif self.amount_tax == 0:
            self.write({
                'state': 'to_review'
            })

    # def button_manager_approve(self):
    #     for order in self:
    #         if order.state not in ['draft', 'sent','manager_approve']:
    #             continue
    #         order._add_supplier_to_product()
    #         # Deal with double validation process
    #         if order.company_id.po_double_validation == 'one_step'\
    #                 or (order.company_id.po_double_validation == 'two_step'\
    #                     and order.amount_total < self.env.company.currency_id._convert(
    #                         order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today()))\
    #                 or order.user_has_groups('purchase.group_purchase_manager'):
    #             order.button_approve()
    #         else:
    #             order.write({'state': 'to approve'})
    #     return True

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

    def button_to_review(self):
        self.write({
            'state': 'cfo_approve'
        })

    def button_tax_review(self):
        self.write({
            'state': 'cfo_approve'
        })

    def button_cfo_reject(self):
        self.write({
            'state': 'reject'
        })


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('to_review', 'Waiting For Review Approval'),
        ('tax_review', 'Waiting For Tax Review Approval'),
        ('cfo_approve', 'Waiting For Approval'),
        ('sale', 'Sales Order'),
        ('reject', 'Reject'),
        ('done', 'Locked'),
        ('cancelled', 'Cancelled'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    def action_confirm(self):
        if self.amount_tax > 0:
            self.write({
                'state': 'tax_review'
            })
        elif self.amount_tax == 0:
            self.write({
                'state': 'to_review'
            })

    def button_cfo_approved(self):
        rec = super(SaleOrderInherit, self).action_confirm()
        return rec

    def button_to_review(self):
        self.write({
            'state': 'cfo_approve'
        })

    def button_tax_review(self):
        self.write({
            'state': 'cfo_approve'
        })

    def button_cfo_reject(self):
        self.write({
            'state': 'reject'
        })


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('to_review', 'Waiting For Review Approval'),
        ('tax_review', 'Waiting For Tax Review Approval'),
        ('cfo_approve', 'Waiting For Approval'),
        ('posted', 'Posted'),
        ('cancel', 'Cancelled'),
        ('reject', 'Rejected'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')

    def action_post(self):
        if self.total_tax_amount > 0:
            self.write({
                'state': 'tax_review'
            })
        elif self.total_tax_amount == 0:
            self.write({
                'state': 'to_review'
            })

    def button_cfo_approved(self):
        rec = super(AccountMoveInherit, self).action_post()
        return rec

    def button_to_review(self):
        self.write({
            'state': 'cfo_approve'
        })

    def button_tax_review(self):
        self.write({
            'state': 'cfo_approve'
        })

    def button_cfo_reject(self):
        self.write({
            'state': 'reject'
        })


class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_review', 'Waiting For Review'),
        ('cfo_approve', 'Waiting For Approval'),
        ('posted', 'Validated'),
        ('sent', 'Sent'),
        ('reconciled', 'Reconciled'),
        ('cancelled', 'Cancelled'),
        ('reject', 'Rejected'),
    ], readonly=True, default='draft', copy=False, string="Status")

    def post(self):
        self.write({
            'state': 'to_review'
        })

    def button_to_review(self):
        self.write({
            'state': 'cfo_approve'
        })
        # res = super(AccountPaymentInherit, self).post()
        # return res

    def button_cfo_approved(self):
        self.pay_post()
        # res = super(AccountPaymentInherit, self).post()
        # return res

    def button_cfo_reject(self):
        self.write({
            'state': 'reject'
        })

    def pay_post(self):
        """ Create the journal items for the payment and update the payment's state to 'posted'.
            A journal entry is created containing an item in the source liquidity account (selected journal's default_debit or default_credit)
            and another in the destination reconcilable account (see _compute_destination_account_id).
            If invoice_ids is not empty, there will be one reconcilable move line per invoice to reconcile with.
            If the payment is a transfer, a second journal entry is created in the destination journal to receive money from the transfer account.
        """
        AccountMove = self.env['account.move'].with_context(default_type='entry')
        for rec in self:

            # if rec.state != 'draft':
            #     raise UserError(_("Only a draft payment can be posted."))

            if any(inv.state != 'posted' for inv in rec.invoice_ids):
                raise ValidationError(_("The payment cannot be processed because the invoice is not open!"))

            # keep the name in case of a payment reset to draft
            if not rec.name:
                # Use the right sequence to set the name
                if rec.payment_type == 'transfer':
                    sequence_code = 'account.payment.transfer'
                else:
                    if rec.partner_type == 'customer':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.customer.invoice'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.customer.refund'
                    if rec.partner_type == 'supplier':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.supplier.refund'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.supplier.invoice'
                rec.name = self.env['ir.sequence'].next_by_code(sequence_code, sequence_date=rec.payment_date)
                if not rec.name and rec.payment_type != 'transfer':
                    raise UserError(_("You have to define a sequence for %s in your company.") % (sequence_code,))

            moves = AccountMove.create(rec._prepare_payment_moves())
            moves.filtered(lambda move: move.journal_id.post_at != 'bank_rec').post()

            # Update the state / move before performing any reconciliation.
            move_name = self._get_move_name_transfer_separator().join(moves.mapped('name'))
            rec.write({'state': 'posted', 'move_name': move_name})

            if rec.payment_type in ('inbound', 'outbound'):
                # ==== 'inbound' / 'outbound' ====
                if rec.invoice_ids:
                    (moves[0] + rec.invoice_ids).line_ids \
                        .filtered(lambda line: not line.reconciled and line.account_id == rec.destination_account_id and not (line.account_id == line.payment_id.writeoff_account_id and line.name == line.payment_id.writeoff_label))\
                        .reconcile()
            elif rec.payment_type == 'transfer':
                # ==== 'transfer' ====
                moves.mapped('line_ids')\
                    .filtered(lambda line: line.account_id == rec.company_id.transfer_account_id)\
                    .reconcile()

        return True
