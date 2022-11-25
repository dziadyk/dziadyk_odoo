from odoo import api, fields, models


class Request(models.Model):
    _name = 'task.tracker.request'
    _inherit = 'task.tracker.status'
    _description = 'Request'
    _rec_name = 'name'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    project_id = fields.Many2one(
        comodel_name='task.tracker.project',
        required=True, )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        related='project_id.partner_id',
        readonly=True,
        store=True, )
    description = fields.Text()
    actual_time = fields.Float(
        compute='_compute_time',
        compute_sudo=True,
        store=True, )
    planed_time = fields.Float(
        compute='_compute_time',
        compute_sudo=True,
        store=True, )
    task_ids = fields.One2many(
        comodel_name='task.tracker.task',
        inverse_name='request_id', )

    # def _compute_project_data(self):
    #     for rec in self:
    #         rec.partner_id = rec.project_id.partner_id
    #
    # @api.onchange('project_id')
    # def _onchange_project_id(self):
    #     self.partner_id = self.project_id.partner_id

    def _compute_time(self):
        for rec in self:
            rec.actual_time = 0
            rec.planed_time = 0
            task_list = self.env['task.tracker.task'].search(
                [('request_id', '=', rec.id)])
            for task in task_list:
                rec.actual_time += task.actual_time
                rec.planed_time += task.planed_time

    @api.onchange('task_ids')
    def _onchange_task_ids(self):
        self.actual_time = 0
        self.planed_time = 0
        task_list = self.env['task.tracker.task'].search(
            [('request_id', '=', self.id)])
        for task in task_list:
            self.actual_time += task.actual_time
            self.planed_time += task.planed_time
