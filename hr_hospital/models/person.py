from odoo import _, fields, models


class Person(models.AbstractModel):
    _name = 'hr.hosp.person'
    _description = 'Person'

    name = fields.Char(
        required=True, )
    gender = fields.Selection(
        selection=[('male', _('Male')),
                   ('female', _('Female')),
                   ('other', _('Other'))],
        required=True, default='other', )
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Image()
