# -*- coding: utf-8 -*-
# Copyright 2016-17 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Stock Orderpoint UoM",
    "summary": "Allows to create procurement orders in the UoM indicated in "
               "the orderpoint",
    "version": "10.0.1.0.2",
    "author": "Eficent, "
              "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/stock-logistics-warehouse",
    "category": "Warehouse Management",
    "depends": ["stock"],
    "data": ["views/stock_warehouse_orderpoint_view.xml"],
    "license": "AGPL-3",
    'installable': True,
    'application': False,
}
