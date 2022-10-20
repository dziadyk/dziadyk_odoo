from odoo import models, fields


class Diagnosis(models.Model):
    _name = 'hr.hosp.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
    active = fields.Boolean(default=True)
    date = fields.Datetime()
    doctor_ids = fields.Many2many(comodel_name='hr.hosp.doctor')
    description = fields.Char()
