from odoo import models, fields


class PatientChart(models.Model):
    _name = 'hr.hosp.patient.chart'
    _description = 'Patient chart'

    name = fields.Char()
    active = fields.Boolean(default=True)
    start_date = fields.Date('Start date')
    finish_date = fields.Date('Finish date')
    diagnosis_ids = fields.Many2many(comodel_name='hr.hosp.diagnosis')
    description = fields.Char()
