from datetime import date
from odoo import api, exceptions, fields, models, _


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(default=True)
    birthday = fields.Date(string='Date of birth', required=True)
    age = fields.Integer(compute='_compute_age')
    passport = fields.Char()
    emergency_contact_ids = fields.Many2many(comodel_name='hr.hosp.emergency.contact', string="Emergency contact")

    @api.constrains('birthday')
    def constrains_birthday(self):
        today = date.today()
        for obj in self:
            if obj.birthday > today:
                raise exceptions.ValidationError(_('Birthday must be less than today'))

    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for obj in self:
            if obj.birthday:
                obj.age = obj.age = today.year - obj.birthday.year - ((today.month, today.day) < (obj.birthday.month, obj.birthday.day))
            else:
                obj.age = 0
