# -*- coding: utf-8 -*-
{
    'name': "resume_app",

    'summary': """
        An application for practicing befor the odoo exam.""",

    'description': """
        An application for practicing befor the odoo exam, but this text is longer.
    """,

    'author': "Josep Pla Sancho",
    'website': "https://open.spotify.com/track/72hcFp4tYkd3dbNA9dZ3Pv?si=bfab1465e0b44575",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/user_view.xml',
        'views/manytomany_view.xml',
        'views/manytoone_view.xml',
        'views/onetomany_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
    'installable' : True,
}

# TYPE OF FIELDS -> Boolean, Float, Char, Text, Date and Selection -> ALL OF THEM IN "user_model"
# TYPE OF PARAMETERS FOR A FIELD: -> string, default, required, index, help, compute, store and selection
