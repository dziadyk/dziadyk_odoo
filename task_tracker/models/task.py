from odoo import api, fields, models


class Task(models.Model):
    _name = 'task.tracker.task'
    _inherit = 'task.tracker.status'
    _description = 'Task'
    _rec_name = 'name'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    request_id = fields.Many2one(
        comodel_name='task.tracker.request',
        required=True, )
    project_id = fields.Many2one(
        comodel_name='task.tracker.project',
        related='request_id.project_id',
        readonly=True,
        store=True, )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        related='request_id.project_id.partner_id',
        readonly=True,
        store=True, )
    description = fields.Text()
    actual_time = fields.Float(
        compute='_compute_time',
        store=True, )
    planed_time = fields.Float(
        required=True, )
    responsible_id = fields.Many2one(
        comodel_name='res.users',
        required=True, )
    team_id = fields.Many2one(
        comodel_name='task.tracker.team',
        related='responsible_id.team_id',
        readonly=True,
        store=True, )
    comment = fields.Text()
    timesheet_ids = fields.One2many(
        comodel_name='task.tracker.timesheet',
        inverse_name='task_id',
        readonly=True, )

    def _compute_time(self):
        for rec in self:
            rec.actual_time = 0
            for timesheet in rec.timesheet_ids:
                rec.actual_time += timesheet.actual_time

    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals)

        # request time
        planed_time = task.planed_time
        time_list = self.env['task.tracker.task'].search([
            ('request_id', '=', task.request_id.id),
            ('id', '!=', task.id)])
        for time in time_list:
            planed_time += time.planed_time
        self.env['task.tracker.request'].browse(task.request_id.id).write(
            {'planed_time': planed_time})

        # project time
        planed_time = task.planed_time
        time_list = self.env['task.tracker.task'].search([
            ('project_id', '=', task.project_id.id),
            ('id', '!=', task.id)])
        for time in time_list:
            planed_time += time.planed_time
        self.env['task.tracker.project'].browse(task.project_id.id).write(
            {'planed_time': planed_time})

        return task

    def write(self, vals):
        task = super(Task, self).write(vals)
        for rec in self:

            # request time
            planed_time = rec.planed_time
            time_list = self.env['task.tracker.task'].search([
                ('request_id', '=', rec.request_id.id),
                ('id', '!=', rec.id)])
            for time in time_list:
                planed_time += time.planed_time
            self.env['task.tracker.request'].browse(rec.request_id.id).write(
                {'planed_time': planed_time})

            # project time
            planed_time = rec.planed_time
            time_list = self.env['task.tracker.task'].search([
                ('project_id', '=', rec.project_id.id),
                ('id', '!=', rec.id)])
            for time in time_list:
                planed_time += time.planed_time
            self.env['task.tracker.project'].browse(rec.project_id.id).write(
                {'planed_time': planed_time})

        return task
