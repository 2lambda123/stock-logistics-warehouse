# -*- coding: utf-8 -*-
# Copyright 2016-2017 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Stock Change Quantity Reason",
    'summary': """
        Stock Quantity Change Reason """,
    'author': 'ACSONE SA/NV, Odoo Community Association (OCA)',
    'website': "https://github.com/OCA/stock-logistics-warehouse",
    'category': 'Warehouse Management',
    'version': '10.0.1.0.1',
    'license': 'AGPL-3',
    'depends': [
        'stock',
    ],
    'data': [
        'wizard/stock_product_change_qty.xml'
    ],
    'installable': True,
}
