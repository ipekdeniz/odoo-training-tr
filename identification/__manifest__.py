# Copyright 2014-2015 Grupo ESOC <www.grupoesoc.es>
# Copyright 2017-Apertoso N.V. (<http://www.apertoso.be>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Identification",
    "summary": "Identification Module",
    'version': '12.0.1.0.0',
    "category": "Identification Management",
    "website": "https://github.com/oca/partner-contact",
    "author": "Grupo ESOC, Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    'application': False,
    'installable': True,
    'auto_install': False,
    "depends": [
        "base","hr"
    ],
    "data": ['security/ir.model.access.csv',
'views/identification_view.xml',
'views/identification_type_view.xml'
             ]
}
