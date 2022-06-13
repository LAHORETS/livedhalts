# -*- coding: utf-8 -*-


from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
from num2words import num2words
from pytz import timezone


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    def amnt_to_text(self, total):
        amnt_txt = self.env.user.company_id.currency_id.amount_to_text(total)
        return amnt_txt

    def get_print_date(self):
        now_utc_date = datetime.now()
        now_dubai = now_utc_date.astimezone(timezone('Asia/Karachi'))
        return now_dubai.strftime('%d/%m%Y %H:%M:%S')


class AccountPaymentInherit(models.Model):
    _inherit = 'account.payment'

    journal_type = fields.Selection([
        ('sale', 'Sales'),
        ('purchase', 'Purchase'),
        ('cash', 'Cash'),
        ('bank', 'Bank'),
        ('general', 'Miscellaneous'),
    ], related='journal_id.type', string='Journal Type')

    user_id = fields.Many2one('res.users', string='Prepared By', default=lambda self: self.env.user.id)

    def dict_values(self):
        res = dict(self.env['account.journal']._fields['type'].selection).get(self.journal_type)
        return res

    def amnt_to_text(self, total):
        amnt_txt = self.env.user.company_id.currency_id.amount_to_text(total)
        # amnt_txt = num2words(total)
        return amnt_txt