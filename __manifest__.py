# -*- coding: utf-8 -*-
{
    'name': "kelompok_bisa",

    'summary': """
        developer-iot.tech
        """,

    'description': """
        Vokasi Universitas Brawijaya
    """,

    'author': "Kelompok Bisa",
    'website': "http://developer-iot.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/prodi.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
