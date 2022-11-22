from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    team_id = fields.Many2one(comodel_name='task.tracker.team', )
