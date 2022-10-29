import datetime
from odoo import _, api, exceptions, fields, models


class DoctorScheduleWizard(models.TransientModel):
    _name = 'hr.hosp.doctor.schedule.wizard'
    _description = 'Doctor Schedule'

    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor',
        required=True, )
    begin_date = fields.Date(
        required=True, )
    end_date = fields.Date(
        required=True, )
    schedule_shift = fields.Selection(
        selection=[('day', 'Day'),
                   ('week', 'Week')],
        required=True, )
    start_time_1 = fields.Float(
        string='Start Time', )
    finish_time_1 = fields.Float(
        string='Finish Time', )
    start_time_2 = fields.Float(
        string='Start Time', )
    finish_time_2 = fields.Float(
        string='Finish Time', )

    def action_open_wizard(self):
        return {
            'name': _('Doctor Schedule'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hosp.doctor.schedule.wizard',
            'target': 'new',
            'context': {},
        }

    def action_create_record(self):
        self.ensure_one()

    @api.constrains('begin_date', 'end_date'
                    'start_time_1', 'finish_time_1',
                    'start_time_2', 'finish_time_2', )
    def constrains_period(self):
        for obj in self:
            if obj.begin_date > obj.end_date:
                raise exceptions.ValidationError(
                    _('Begin date must be less end date'))
            if obj.start_time_1 >= obj.finish_time_1 \
                    or obj.start_time_2 >= obj.finish_time_2:
                raise exceptions.ValidationError(
                    _('Start time must be less than finish'))
