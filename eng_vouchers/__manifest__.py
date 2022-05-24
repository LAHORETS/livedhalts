# -*- coding: utf-8 -*-
{
    'name': "Engine Account Vouchers",

    'summary': """
        Create 5 voucher print as sample attached named bank,cash (Payment and Receipt.) and general journal
    """,

    'description': """
        Create 5 voucher print as sample attached named bank,cash (Payment and receipt.) and general journal
        Cash Receipt Voucher
        Cash Payment Voucher
        Bank Receipt Voucher
        Bank Payment Voucher
        General journal
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'views/voucher_views.xml',
        'reports/cash_receipt_report.xml',
        'reports/cash_receipt_template.xml',
        'reports/journal_entry_report.xml',
        'reports/journal_entry_template.xml',
    ],

}
