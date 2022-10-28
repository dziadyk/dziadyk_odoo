from odoo import fields, models


class SampleType(models.Model):
    _name = 'hr.hosp.sample.type'
    _description = 'Sample Type'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
