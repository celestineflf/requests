# -*- coding: utf-8 -*-
{
    'name': 'Requests',
    'version': '1.0',
    'category': 'Productivity',
    'summary': 'Ticketssss',
    'sequence': '-100',

    'depends': [
        'mail',
        'calendar',
        'sale',
    ],

    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/menu_actions.xml',
        'views/ticket_views.xml',
        'views/sales_views.xml',
        'views/logistic_views.xml',
        'views/finance_views.xml',
        'views/purchase_views.xml',
        'views/support_views.xml',
        'views/management_views.xml',
        'views/main_menu_view.xml',
        
    ],

    'author': 'Celestine Dabrowski',
    'maintainer': 'Celestine Dabrowski',

    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
