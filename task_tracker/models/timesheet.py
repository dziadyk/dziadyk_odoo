import datetime

from odoo import api, exceptions, fields, models, _


class Timesheet(models.Model):
    _name = 'task.tracker.timesheet'
    _description = 'Timesheet'

    active = fields.Boolean(
        default=True, )
    date = fields.Date(
        default=datetime.datetime.today(),
        required=True, )
    responsible_id = fields.Many2one(
        comodel_name='res.users',
        default=lambda self: self.env.user,
        required=True, )
    team_id = fields.Many2one(
        comodel_name='task.tracker.team',
        compute='_compute_team', )
    actual_time = fields.Float(
        required=True, )
    task_id = fields.Many2one(
        comodel_name='task.tracker.task',
        required=True, )
    request_id = fields.Many2one(
        comodel_name='task.tracker.request',
        compute='_compute_task_data',
        store=True, )
    project_id = fields.Many2one(
        comodel_name='task.tracker.project',
        compute='_compute_task_data',
        store=True, )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        compute='_compute_task_data',
        store=True, )

    comment = fields.Text()

    def _compute_task_data(self):
        for rec in self:
            rec.request_id = rec.task_id.request_id
            rec.project_id = rec.request_id.project_id
            rec.partner_id = rec.project_id.partner_id

    @api.onchange('task_id')
    def _onchange_request_id(self):
        self.request_id = self.task_id.request_id
        self.project_id = self.request_id.project_id
        self.partner_id = self.project_id.partner_id

    def _compute_team(self):
        for rec in self:
            rec.team_id = rec.responsible_id.team_id

    @api.onchange ('responsible_id')
    def _onchange_responsible_id(self):
        self.team_id = self.responsible_id.team_id
        if self.task_id and self.task_id.responsible_id != self.responsible_id:
            self.task_id = False

    def name_get(self):
        name_list = []
        for rec in self:
            timesheet_name = "{} ({}) {}".format(
                rec.responsible_id.name,
                rec.date,
                rec.task_id.name, )
            name_list.append((rec.id, timesheet_name))
        return name_list

    @api.constrains('actual_time')
    def constrains_lead_is_member(self):
        for rec in self:
            if rec.actual_time == 0:
                raise exceptions.ValidationError(
                    _('Actual Time can not be 00:00'))

    @api.model
    def create(self, vals):
        timesheet = super(Timesheet, self).create(vals)

        # task time
        actual_time = timesheet.actual_time
        time_list = self.env['task.tracker.timesheet'].search([
            ('task_id', '=', timesheet.task_id.id),
            ('id', '!=', timesheet.id)])
        for time in time_list:
            actual_time += time.actual_time
        self.env['task.tracker.task'].browse(timesheet.task_id.id).write(
            {'actual_time': actual_time})

        # request time
        actual_time = timesheet.actual_time
        time_list = self.env['task.tracker.timesheet'].search([
            ('request_id', '=', timesheet.request_id.id),
            ('id', '!=', timesheet.id)])
        for time in time_list:
            actual_time += time.actual_time
        self.env['task.tracker.request'].browse(timesheet.request_id.id).write(
            {'actual_time': actual_time})

        # project time
        actual_time = timesheet.actual_time
        time_list = self.env['task.tracker.timesheet'].search([
            ('project_id', '=', timesheet.project_id.id),
            ('id', '!=', timesheet.id)])
        for time in time_list:
            actual_time += time.actual_time
        self.env['task.tracker.project'].browse(timesheet.project_id.id).write(
            {'actual_time': actual_time})

        return timesheet

    def write(self, vals):
        timesheet = super(Timesheet, self).write(vals)
        for rec in self:

            # task time
            actual_time = rec.actual_time
            time_list = self.env['task.tracker.timesheet'].search([
                ('task_id', '=', rec.task_id.id),
                ('id', '!=', rec.id)])
            for time in time_list:
                actual_time += time.actual_time
            self.env['task.tracker.task'].browse(rec.task_id.id).write(
                {'actual_time': actual_time})

            # request time
            actual_time = rec.actual_time
            time_list = self.env['task.tracker.timesheet'].search([
                ('request_id', '=', rec.request_id.id),
                ('id', '!=', rec.id)])
            for time in time_list:
                actual_time += time.actual_time
            self.env['task.tracker.request'].browse(rec.request_id.id).write(
                {'actual_time': actual_time})

            # project time
            actual_time = rec.actual_time
            time_list = self.env['task.tracker.timesheet'].search([
                ('project_id', '=', rec.project_id.id),
                ('id', '!=', rec.id)])
            for time in time_list:
                actual_time += time.actual_time
            self.env['task.tracker.project'].browse(rec.project_id.id).write(
                {'actual_time': actual_time})

        return timesheet
