# -*- coding: utf-8 -*-
from openerp import http

# class L10nVeAdministrative(http.Controller):
#     @http.route('/l10n_ve_administrative/l10n_ve_administrative/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ve_administrative/l10n_ve_administrative/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ve_administrative.listing', {
#             'root': '/l10n_ve_administrative/l10n_ve_administrative',
#             'objects': http.request.env['l10n_ve_administrative.l10n_ve_administrative'].search([]),
#         })

#     @http.route('/l10n_ve_administrative/l10n_ve_administrative/objects/<model("l10n_ve_administrative.l10n_ve_administrative"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ve_administrative.object', {
#             'object': obj
#         })