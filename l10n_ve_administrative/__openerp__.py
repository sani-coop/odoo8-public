# -*- coding: utf-8 -*-

{
    'name': "Venezuela - States, Municipalities and Parishes",

    'summary': """
        Add States, Municipalities and Parishes to Odoo Base models""",

    'description': """
        Based on INE information
        http://www.ine.gov.ve/documentos/AspectosFisicos/DivisionpoliticoTerritorial/pdf/DPTconFinesEstadisticosOperativa2013.pdf

        Adds a dropdown list of Municipalities on the partner form views (and all
        its derivatives), filtered by State. And a dropdown list of pariches
        filtered by Municipality.
    """,

    'author': "Cooperativa Saní Tecnologías Comunes",
    'website': "http://sani.org.ve",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/res_partner.xml',
        'views/res_country.xml',
        'data/res.country.state.csv',
        'data/res.country.state.municipality.csv',
        'data/res.country.state.municipality.parish.csv',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
