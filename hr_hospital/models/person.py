from odoo import fields, models


class Person(models.AbstractModel):
    _name = 'hr.hosp.person'
    _description = 'Person'

    name = fields.Char(
        required=True, )
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        required=True, default='other', )
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Image()
