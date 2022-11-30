from odoo import fields, models


class ResUsers(models.Model):
    """Inherit model res.users
    Add user's team
    """
    _inherit = 'res.users'

    team_id = fields.Many2one(
        comodel_name='task.tracker.team',
        ondelete="set null", )
