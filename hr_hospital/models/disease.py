from odoo import fields, models


class Disease(models.Model):
    _name = 'hr.hosp.disease'
    _description = 'Disease'

    name = fields.Char(required=True)
    disease_type_id = fields.Many2one(comodel_name='hr.hosp.disease.type', string='Type')
    active = fields.Boolean(default=True)
