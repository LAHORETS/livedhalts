# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    discount_account_invoice = fields.Many2one(
        string="Income TaxAccount",
        comodel_name='account.account',
        help="Income Tax discount on invoices.")
    discount_account_bill = fields.Many2one(
        string="Income Tax Account",
        comodel_name='account.account',
        help="Account for Income Tax on bills.")
