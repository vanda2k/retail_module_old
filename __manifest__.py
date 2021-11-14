# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Retail Module',
    'version': '1.0',
    'summary': 'Odoo Project Retail Management',
    'sequence': 1,
    'author': 'Đỗ Anh Văn + Nguyễn Thị Thảo',
    'description': """
        Odoo Project
    """,
    'category': 'Other',
    'website': '',
    'depends': [],
    'data': [
        'views/product_view.xml',
        'views/category_view.xml',
        'views/unit_view.xml',
        'views/employee_view.xml',
        'views/position_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
        'views/supplier_view.xml',
        'views/purchase_view.xml',
    ],
    'installable': True,
    'application': True,
}
