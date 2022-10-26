from odoo import fields, models


class Doctor(models.Model):
    _name = 'hr.hosp.doctor'
    _description = 'Doctor'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    specialty = fields.Char()
