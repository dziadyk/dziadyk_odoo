from odoo import fields, models


class MedicalTest(models.Model):
    _name = 'hr.hosp.medical.test'
    _description = 'Medical Test'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    medical_test_type_id = fields.Many2one(
        comodel_name='hr.hosp.medical.test.type', string='Type', )
    patient_id = fields.Many2one(
        comodel_name='hr.hosp.patient', required=True, )
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', required=True, )
    sample_type = fields.Many2one(
        comodel_name='hr.hosp.sample.type', )
    sample = fields.Char()
    report = fields.Text()
