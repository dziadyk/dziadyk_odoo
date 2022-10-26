from odoo import fields, models, _


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'

    name = fields.Char()
    active = fields.Boolean(default=True)
    sex = fields.Selection([('male','Male'),('female','Female'),('other','Other')],required=True,default='other')
    birthday = fields.Date(string='Date of birth',required=True)
    age = fields.Integer()
    chart_ids = fields.Many2many(comodel_name='hr.hosp.patient.chart')
