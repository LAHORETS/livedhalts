# -*- coding: utf-8 -*-
# from odoo import http


# class Custom(http.Controller):
#     @http.route('/custom/custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom/custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom.listing', {
#             'root': '/custom/custom',
#             'objects': http.request.env['custom.custom'].search([]),
#         })

#     @http.route('/custom/custom/objects/<model("custom.custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom.object', {
#             'object': obj
#         })
