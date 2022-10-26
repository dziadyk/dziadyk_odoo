from odoo import fields, models


class EmergencyContact(models.Model):
    _name = 'hr.hosp.emergency.contact'
    _description = 'Emergency contact'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(default=True)
    description = fields.Text()
