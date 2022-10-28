from odoo import fields, models


class Diagnosis(models.Model):
    _name = 'hr.hosp.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    date = fields.Datetime()
    patient_id = fields.Many2one(
        comodel_name='hr.hosp.patient', required=True, )
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', required=True, )
    disease_id = fields.Many2one(
        comodel_name='hr.hosp.disease', )
    medical_test_ids = fields.Many2many(
        comodel_name='hr.hosp.medical.test', )
    treatment = fields.Text()
    is_intern = fields.Boolean(
        related="doctor_id.is_intern", )
    mentor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', related="doctor_id.mentor_id", )
    mentor_comment = fields.Text(
        string="Comment", )
