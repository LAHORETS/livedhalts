# -*- coding: utf-8 -*-
{
    'name': "Custom Payroll",

    'summary': """
        This Module Contains Main Custom Functionalities of LTS Payroll""",

    'description': """
        This Module Contains Main Custom Functionalities of LTS Payroll
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'All',
    'version': '13.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_payroll', 'hr_contract', 'hr'],

    # always loaded
    'data': [
        'views/payroll_views.xml',
        # 'reports/payslip_report.xml',
        # 'reports/payslip_template.xml',
    ],

}
