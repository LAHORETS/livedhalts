# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLineInh(models.Model):
    _inherit = 'account.move.line'

    # @api.model
    # def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        # if not self.check_access_rights('read', False):
        #     referral_fields = {
        #         'name', 'partner_name', 'job_id', 'referral_points_ids', 'earned_points', 'max_points',
        #         'shared_item_infos', 'referral_state', 'user_id', 'friend_id', '__last_update'}
        #     if not set(fields or []) - referral_fields and self.env.user:
        #         domain = expression.AND([domain, [('ref_user_id', '=', self.env.user.id)]])
        #         return super(Applicant, self.sudo()).search_read(domain=domain, fields=fields, offset=offset,
        #                                                          limit=limit, order=order)
        # journal = self.env['account.journal'].search([('name', '=', 'Inventory Valuation')], limit=1)
        # domain = [('journal_id', '=', 47)]
        # print(domain)
        # return super(AccountMoveLineInh, self).search_read(domain=domain)
        # return super().search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)

