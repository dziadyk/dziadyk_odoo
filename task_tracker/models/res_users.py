from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'
    # _parent_name = 'team_id'
    # _parent_store = True

    team_id = fields.Many2one(
        comodel_name='task.tracker.team',
        ondelete="set null", )
