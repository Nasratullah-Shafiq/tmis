{
    'name': 'Tailor Management',
    'version': '17.0.1.0.0',
    'summary': 'Manage tailor customers, measurements, orders and staff',
    'description': 'Tailor Management System for Odoo 17 - customers, measurements, orders, staff assignment and basic inventory link',
    'category': 'Services',
    'author': 'Nasratullah Shafiq',
    'depends': ['base', 'mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/tailor_menu.xml',
        'views/customer_views.xml',
        'views/measurement_views.xml',
        'views/order_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}
