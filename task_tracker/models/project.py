from odoo import fields, models


class Project(models.Model):
    _name = 'task.tracker.project'
    _inherit = 'task.tracker.status'
    _description = 'Project'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=True, )
    description = fields.Text()
