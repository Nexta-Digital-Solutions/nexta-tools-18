# -*- coding: utf-8 -*-
{
    'name': "stock_picking_normativa_deca",
    'summary': "Generación básica de albaranes DeCA versionados",
    'description': "Generación básica de albaranes DeCA versionados",
    'author': "NextaDS",
    'website': "https://www.nextads.es",
    'category': 'Inventory',
    'version': '18.0.0.5',
    'license': "LGPL-3",
    'depends': [
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/stock_picking_deca_report.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
}
