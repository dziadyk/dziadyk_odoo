from odoo import fields, models


class Diagnosis(models.Model):
    _name = 'hr.hosp.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    patient_id = fields.Many2one(comodel_name='hr.hosp.patient',required=True)
    doctor_id = fields.Many2one(comodel_name='hr.hosp.doctor',required=True)
    disease = fields.Char()
    date = fields.Datetime()
    treatment = fields.Text()
