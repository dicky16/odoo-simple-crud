# -*- coding: utf-8 -*-
from odoo import http


class KelompokBisa(http.Controller):
    @http.route('/kelompok_bisa/kelompok_bisa/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/kelompok_bisa/kelompok_bisa/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('kelompok_bisa.listing', {
            'root': '/kelompok_bisa/kelompok_bisa',
            'objects': http.request.env['kelompok_bisa.kelompok_bisa'].search([]),
        })

    @http.route('/kelompok_bisa/kelompok_bisa/objects/<model("kelompok_bisa.kelompok_bisa"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('kelompok_bisa.object', {
            'object': obj
        })
