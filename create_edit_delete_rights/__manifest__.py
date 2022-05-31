# -*- coding: utf-8 -*-
{
    'name': "Create Edit Delete Rights",

    'summary': """
        Remove Create Edit Delete Rights""",

    'description': """
        Remove Create Edit Delete Rights
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'All',
    'version': '13.0.0.0',
    "sequence":  1,

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'account', 'stock', 'purchase'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/views.xml',
    ],

}
