# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError, UserError

class DocumentAttachmentCustomValidate(models.Model):
    _inherit = "ir.attachment"

    @api.model_create_multi
    def create(self, vals_list):
        if len(vals_list) > 0 and 'name' in vals_list[0]:
            prev_files = self.env['documents.document'].search([]).mapped('name')
            if vals_list[0]['name'] in prev_files:
                raise UserError(_('file already existed'))
            else:
                res = super(DocumentAttachmentCustomValidate, self).create(vals_list)
                return res

