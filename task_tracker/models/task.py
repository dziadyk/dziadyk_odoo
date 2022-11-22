from odoo import api, fields, models


class Task(models.Model):
    _name = 'task.tracker.task'
    _inherit = 'task.tracker.status'
    _description = 'Task'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    request_id = fields.Many2one(
        comodel_name='task.tracker.request',
        required=True, )
    project_id = fields.Many2one(
        comodel_name='task.tracker.project',
        compute='_compute_request_data', )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        compute='_compute_request_data', )
    description = fields.Text()
    planed_time = fields.Float()
    actual_time = fields.Float()
    responsible_id = fields.Many2one(
        comodel_name='res.users',
        required=True, )
    team_id = fields.Many2one(
        comodel_name='task.tracker.team',
        compute='_compute_team', )

    def _compute_request_data(self):
        for rec in self:
            rec.project_id = rec.request_id.project_id
            rec.partner_id = rec.project_id.partner_id

    @api.onchange('request_id')
    def _onchange_request_id(self):
        self.team_id = self.responsible_id.team_id

    def _compute_team(self):
        for rec in self:
            rec.team_id = rec.responsible_id.team_id

    @api.onchange ('responsible_id')
    def _onchange_responsible_id(self):
        self.team_id = self.responsible_id.team_id
