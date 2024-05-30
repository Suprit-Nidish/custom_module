# -*- coding: utf-8 -*-
{
    'name' : 'Sale Bulk Update',
    'version' : '1.0',
    'author' : 'Suprit-S',
    'summary': 'Sale columns bulk update using server action',
    'sequence': 1,
    'description': """
    Sale columns bulk update using server action
    """,
    'category': 'Sales',
    'website': '',
    'images' : [],
    'depends' : ['sale'],
    'data': [
        'views/sale_bulk_update.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}