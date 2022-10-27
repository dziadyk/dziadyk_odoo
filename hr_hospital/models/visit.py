from odoo import fields, models


class Visit(models.Model):
    _name = 'hr.hosp.visit'
    _description = 'Visit'

    active = fields.Boolean(default=True)
    doctor_id = fields.Many2one(comodel_name='hr.hosp.doctor', required=True)
    patient_id = fields.Many2one(comodel_name='hr.hosp.patient', required=True)
    diagnosis_ids = fields.Many2many(comodel_name='hr.hosp.diagnosis')
    reception_time = fields.Datetime(required=True)
    recommendation = fields.Text()
