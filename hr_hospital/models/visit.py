from odoo import api, exceptions, fields, models, _


class Visit(models.Model):
    _name = 'hr.hosp.visit'
    _description = 'Visit'
    _rec_name = 'patient_id'

    active = fields.Boolean(
        default=True, )
    planed_date = fields.Date()
    reception_time = fields.Datetime()
    take_place = fields.Boolean()
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', required=True, )
    patient_id = fields.Many2one(
        comodel_name='hr.hosp.patient', required=True, )
    diagnosis_ids = fields.Many2many(
        comodel_name='hr.hosp.diagnosis', )
    medical_test_ids = fields.Many2many(
        comodel_name='hr.hosp.medical.test', )
    recommendation = fields.Text()

    @api.constrains('planed_date', 'reception_time', 'doctor_id', 'patient_id')
    def constrains_take_place(self):
        for obj in self:
            if obj.take_place:
                raise exceptions.ValidationError(
                    _('The visit has already taken place'))
