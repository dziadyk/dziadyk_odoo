from datetime import date
from odoo import api, exceptions, fields, models, _


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(default=True)
    birthday = fields.Date(string='Date of Birth', required=True)
    age = fields.Integer(compute='_compute_age')
    passport = fields.Char()
    personal_doctor_id = fields.Many2one(comodel_name='hr.hosp.doctor')
    emergency_contact_ids = fields.Many2many(comodel_name='hr.hosp.emergency.contact')

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for obj in self:
            if obj.birthday:
                obj.age = obj.age = today.year - obj.birthday.year - (
                            (today.month, today.day) < (obj.birthday.month, obj.birthday.day))
            else:
                obj.age = 0

    @api.constrains('birthday')
    def constrains_birthday(self):
        today = date.today()
        for obj in self:
            if obj.birthday > today:
                raise exceptions.ValidationError(_('Birthday must be less than today'))
