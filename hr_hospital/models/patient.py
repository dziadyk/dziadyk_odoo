import datetime
from odoo import api, exceptions, fields, models, _


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(
        default=True, )
    birthday = fields.Date(
        string='Date of Birth', required=True, )
    age = fields.Integer(
        compute='_compute_age', )
    passport = fields.Char()
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', string='Personal Doctor', )
    emergency_contact_ids = fields.Many2many(
        comodel_name='hr.hosp.emergency.contact', )

    def write(self, vals):
        patient = super(Patient, self).write(vals)
        if vals.get('doctor_id'):
            doctor_history_dict = {
                'patient_id': self.id,
                'doctor_id': vals['doctor_id'],
                'datetime': datetime.datetime.now()
            }
            self.env['hr.hosp.personal.doctor.history']\
                .create(doctor_history_dict)
        return patient

    @api.constrains('birthday')
    def constrains_birthday(self):
        today = datetime.date.today()
        for obj in self:
            if obj.birthday > today:
                raise exceptions.ValidationError(
                    _('Birthday must be less than today'))

    @api.depends('birthday')
    def _compute_age(self):
        today = datetime.date.today()
        for obj in self:
            if obj.birthday:
                extra_year = ((today.month, today.day)
                              < (obj.birthday.month, obj.birthday.day))
                obj.age = today.year - obj.birthday.year - extra_year
            else:
                obj.age = 0

    @api.model
    def create(self, vals):
        patient = super(Patient, self).create(vals)
        if vals['doctor_id']:
            doctor_history_dict = {
                'patient_id': patient.id,
                'doctor_id': vals['doctor_id'],
                'datetime': datetime.datetime.now()
            }
            self.env['hr.hosp.personal.doctor.history']\
                .create(doctor_history_dict)
        return patient
