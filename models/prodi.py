from odoo import models, fields, api

class Prodi(models.Model):
    _name  = 'prodi.ub'
    _deskripsi = 'Data prodi Vokasi UB'
    name = fields.Text(string='Nama Prodi', required = True, helps='Input nama prodi')