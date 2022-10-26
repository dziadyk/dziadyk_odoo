from odoo import fields, models


class PatientChart(models.Model):
    _name = 'hr.hosp.patient.chart'
    _description = 'Patient chart'

    name = fields.Char()
    active = fields.Boolean(default=True)
    start_date = fields.Date()
    finish_date = fields.Date()
    diagnosis_ids = fields.Many2many(comodel_name='hr.hosp.diagnosis')
    description = fields.Char()
