# -*- coding: utf-8 -*-
{
    'name': "Modo de pago en sale order Odoo 15",

    'summary': """
        Estamos probando como crear un modulo en odoo 15 para probar que tal funciona esto.""",

    'description': """
        Creando modulo para aprender.
    """,

    'author': "Nacho Garcia",
    'website': "http://www.eldiestro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_order_view.xml'
    ],

}
