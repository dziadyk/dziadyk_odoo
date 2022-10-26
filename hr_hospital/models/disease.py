from odoo import fields, models


class Disease(models.Model):
    _name = 'hr.hosp.disease'
    _description = 'Disease'

    name = fields.Char()
    active = fields.Boolean(default=True)
