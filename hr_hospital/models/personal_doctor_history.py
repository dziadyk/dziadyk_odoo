from odoo import fields, models


class PersonalDoctorHistory(models.Model):
    _name = 'hr.hosp.personal.doctor.history'
    _description = 'Personal doctor history'

    active = fields.Boolean(default=True)
    patient_id = fields.Many2one(comodel_name='hr.hosp.patient', required=True)
    doctor_id = fields.Many2one(comodel_name='hr.hosp.doctor', required=True)
    date = fields.Datetime(required=True)
