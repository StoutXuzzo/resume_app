# -*- coding: utf-8 -*-
# from odoo import http


# class ResumeApp(http.Controller):
#     @http.route('/resume_app/resume_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/resume_app/resume_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('resume_app.listing', {
#             'root': '/resume_app/resume_app',
#             'objects': http.request.env['resume_app.resume_app'].search([]),
#         })

#     @http.route('/resume_app/resume_app/objects/<model("resume_app.resume_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('resume_app.object', {
#             'object': obj
#         })
