# -*- coding: utf-8 -*-
{
    'name': "Approve Limits",

    'summary': """
       Create an Approval on PO Biils Payments to approve the respective documents""",

    'description': """
       Create an Approval on PO Biils Payments to approve the respective documents
    """,

    'author': "Viltco",
    'website': "https://viltco.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'all',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'sale', 'account'],

    # always loaded
    'data': [
        'security/security.xml',
        'views/approve_limit_views.xml',
    ],

}
