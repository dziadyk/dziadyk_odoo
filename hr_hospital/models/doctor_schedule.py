from odoo import fields, models


class DoctorSchedule(models.Model):
    _name = 'hr.hosp.doctor.schedule'
    _description = 'Doctor Schedule'
    _rec_name = 'doctor_id'

    active = fields.Boolean(
        default=True, )
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', )
    date = fields.Date()
    start_time = fields.Float()
    finish_time = fields.Float()
