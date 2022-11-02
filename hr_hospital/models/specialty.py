from odoo import fields, models


class Specialty(models.Model):
    _name = 'hr.hosp.specialty'
    _description = 'Specialty'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
