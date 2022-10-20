from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr.hosp.doctor'
    _description = 'Doctor'

    name = fields.Char()
    active = fields.Boolean(default=True)
    specialty = fields.Char()
