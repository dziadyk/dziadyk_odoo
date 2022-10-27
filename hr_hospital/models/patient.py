import datetime
from odoo import api, exceptions, fields, models, _


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(default=True)
    birthday = fields.Date(string='Date of Birth', required=True)
    age = fields.Integer(compute='_compute_age')
    passport = fields.Char()
    doctor_id = fields.Many2one(comodel_name='hr.hosp.doctor', string='Personal Doctor')
    emergency_contact_ids = fields.Many2many(comodel_name='hr.hosp.emergency.contact')

    def write(self, vals):
        if vals.get('doctor_id'):
            doctor_history_dict = {
                'patient_id': vals['doctor_id'],
                'doctor_id': self.id,
                'datetime': datetime.datetime.now()
            }
            self.env['hr.hosp.personal.doctor.history'].create(doctor_history_dict)
        return super(Patient, self).write(vals)

    @api.depends('birthday')
    def _compute_age(self):
        today = datetime.date.today()
        for obj in self:
            if obj.birthday:
                obj.age = obj.age = today.year - obj.birthday.year - (
                        (today.month, today.day) < (obj.birthday.month, obj.birthday.day))
            else:
                obj.age = 0

    @api.constrains('birthday')
    def constrains_birthday(self):
        today = datetime.date.today()
        for obj in self:
            if obj.birthday > today:
                raise exceptions.ValidationError(_('Birthday must be less than today'))
