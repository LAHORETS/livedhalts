# -*- coding: utf-8 -*-
{
    'name': "Employee Partner Creation",

    'summary': """
        Create A Partner on Employee Creation""",

    'description': """
        Create A Partner on Employee Creation
    """,

    'author': "Musadiq Chaudhary",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'hr',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/views.xml',
    ],

}
