from datetime import timedelta

from odoo import models, fields, api


class Identification(models.Model):
    _name = 'identification'
    _description = 'Identification'

    employee_id = fields.Many2one("hr.employee", string='Employee')
    identification_type_id = fields.Many2one("identification.type",string='Identification Type')
    identification_number = fields.Char(string = 'Identification Number')
