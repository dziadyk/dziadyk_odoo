from odoo import api, fields, models


class Project(models.Model):
    _name = 'task.tracker.project'
    _inherit = 'task.tracker.status'
    _description = 'Project'
    _rec_name = 'name'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        required=True, )
    description = fields.Text()
    actual_time = fields.Float(
        compute='_compute_time',
        compute_sudo=True,
        store=True, )
    planed_time = fields.Float(
        compute='_compute_time',
        compute_sudo=True,
        store=True,)
    request_ids = fields.One2many(
        comodel_name='task.tracker.request',
        inverse_name='project_id', )

    def _compute_time(self):
        for rec in self:
            rec.actual_time = 0
            rec.planed_time = 0
            for request in rec.request_ids:
                rec.actual_time += request.actual_time
                rec.planed_time += request.planed_time

    @api.onchange('request_ids')
    def _onchange_project_id(self):
        self.actual_time = 0
        self.planed_time = 0
        for request in self.request_ids:
            self.actual_time += request.actual_time
            self.planed_time += request.planed_time
