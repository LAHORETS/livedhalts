# -*- coding: utf-8 -*-
# from odoo import http


# class DefaultDocumentTree(http.Controller):
#     @http.route('/default_document_tree/default_document_tree/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_document_tree/default_document_tree/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_document_tree.listing', {
#             'root': '/default_document_tree/default_document_tree',
#             'objects': http.request.env['default_document_tree.default_document_tree'].search([]),
#         })

#     @http.route('/default_document_tree/default_document_tree/objects/<model("default_document_tree.default_document_tree"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_document_tree.object', {
#             'object': obj
#         })
