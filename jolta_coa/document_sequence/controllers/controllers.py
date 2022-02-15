# -*- coding: utf-8 -*-
# from odoo import http


# class DocumentSequence(http.Controller):
#     @http.route('/document_sequence/document_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document_sequence/document_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('document_sequence.listing', {
#             'root': '/document_sequence/document_sequence',
#             'objects': http.request.env['document_sequence.document_sequence'].search([]),
#         })

#     @http.route('/document_sequence/document_sequence/objects/<model("document_sequence.document_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document_sequence.object', {
#             'object': obj
#         })
