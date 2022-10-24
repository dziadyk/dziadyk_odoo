from odoo import models, fields


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'

    name = fields.Char()
    active = fields.Boolean(default=True)
    birthday = fields.Date('Date of birth')
    chart_ids = fields.Many2many(comodel_name='hr.hosp.patient.chart')
