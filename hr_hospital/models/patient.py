from odoo import fields, models


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    sex = fields.Selection([('male','Male'),('female','Female'),('other','Other')],required=True,default='other')
    birthday = fields.Date(string='Date of birth',required=True)
    age = fields.Integer()
    passport = fields.Char()
    emergency_contact_ids = fields.Many2many(comodel_name='hr.hosp.emergency.contact')
