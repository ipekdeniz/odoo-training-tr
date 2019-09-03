from datetime import timedelta

from odoo import models, fields, api


class Identification(models.Model):
    _name = 'identification.type'
    _description = 'Identification Type'


    type = fields.Char(string = 'Identification Type')
    