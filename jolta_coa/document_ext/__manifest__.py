# -*- coding: utf-8 -*-

{
    'name': 'Document Extension',
    'version': '13.0.1.0',
    'category': 'Operations/Documents',
    'summary': """Increase width of Search Panel""",
    'description': """
Increase width of Search Panel
==================
This app increases width of Search Panel.
""",
    'depends': ['documents'],
    'data': [
        'views/assets.xml',
    ],
     'qweb': [
        "static/src/xml/*.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
