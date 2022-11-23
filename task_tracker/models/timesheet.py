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
        compute='_compute_task_data', )
    project_id = fields.Many2one(
        comodel_name='task.tracker.project',
        compute='_compute_task_data', )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        compute='_compute_task_data', )

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
