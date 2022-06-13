# -*- coding: utf-8 -*-

{
    'name': 'LTS Advances Management',
    'version': '13.0.0.0',
    'summary': 'Manage Advances Requests',
    'description': """
        Helps you to manage Advances Requests of your company's staff.
        """,
    'category': 'Hr',
    'author': "Viltco",
    'company': 'Viltco',
    'maintainer': 'Viltco',
    'website': "https://www.viltco.com",
    'depends': [
        'base', 'hr', 'account', 'payslip_payroll'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/hr_loan_seq.xml',
        'data/salary_rule_loan.xml',
        'views/hr_advances.xml',
        'views/hr_payroll.xml',
    ],
    'demo': [],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
