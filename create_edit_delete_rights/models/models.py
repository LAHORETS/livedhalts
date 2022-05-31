# -*- coding: utf-8 -*-


import calendar
from lxml import etree
from odoo import models, fields, api
from datetime import datetime


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(HrEmployeeInherit, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar,
            submenu=submenu)
        if not self.env.user.has_group('create_edit_delete_rights.group_employee_rights'):
            temp = etree.fromstring(result['arch'])
            # temp.set('create', '0')
            temp.set('edit', '0')
            temp.set('delete', '0')
            result['arch'] = etree.tostring(temp)
        return result


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(AccountMoveInherit, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar,
            submenu=submenu)
        if not self.env.user.has_group('create_edit_delete_rights.group_invoice_bill_rights'):
            temp = etree.fromstring(result['arch'])
            # temp.set('create', '0')
            temp.set('edit', '0')
            temp.set('delete', '0')
            result['arch'] = etree.tostring(temp)
        return result


class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(AccountPaymentInherit, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar,
            submenu=submenu)
        if not self.env.user.has_group('create_edit_delete_rights.group_payment_rights'):
            temp = etree.fromstring(result['arch'])
            # temp.set('create', '0')
            temp.set('edit', '0')
            temp.set('delete', '0')
            result['arch'] = etree.tostring(temp)
        return result


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(StockPickingInherit, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar,
            submenu=submenu)
        if not self.env.user.has_group('create_edit_delete_rights.group_transfer_rights'):
            temp = etree.fromstring(result['arch'])
            # temp.set('create', '0')
            temp.set('edit', '0')
            temp.set('delete', '0')
            result['arch'] = etree.tostring(temp)
        return result


class POInherit(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(POInherit, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar,
            submenu=submenu)
        if not self.env.user.has_group('create_edit_delete_rights.group_purchase_order_rights'):
            temp = etree.fromstring(result['arch'])
            # temp.set('create', '0')
            temp.set('edit', '0')
            temp.set('delete', '0')
            result['arch'] = etree.tostring(temp)
        return result