# -*- coding: utf-8 -*-
{
    'name': "document_sequence",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Erum Asghar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','documents'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/document_server_action.xml',
        'views/document_sequence.xml',
      
        
    ],
    
    'qweb': [
        'static/src/xml/list_view_buttons.xml',
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
