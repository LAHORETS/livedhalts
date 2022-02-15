# -*- coding: utf-8 -*-
# from odoo import http


# class DocumentValidation(http.Controller):
#     @http.route('/document_validation/document_validation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document_validation/document_validation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('document_validation.listing', {
#             'root': '/document_validation/document_validation',
#             'objects': http.request.env['document_validation.document_validation'].search([]),
#         })

#     @http.route('/document_validation/document_validation/objects/<model("document_validation.document_validation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document_validation.object', {
#             'object': obj
#         })
