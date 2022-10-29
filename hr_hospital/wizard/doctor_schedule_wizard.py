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

        day_to_shift = 1
        if self.schedule_shift == 'week':
            day_to_shift = 7
        shift1 = True
        cur_date = self.begin_date
        while cur_date <= self.end_date:

            cur_start = self.start_time_1
            cur_finish = self.finish_time_1
            if not shift1:
                cur_start = self.start_time_2
                cur_finish = self.finish_time_2

            self.env['hr.hosp.doctor.schedule'].create(
                {'doctor_id': self.doctor_id.id,
                 'date': cur_date,
                 'start_time': cur_start,
                 'finish_time': cur_finish})

            cur_date += datetime.timedelta(days=1)
            if day_to_shift <= cur_date.isocalendar()[2]:
                shift1 = not shift1

    @api.constrains('begin_date', 'end_date'
                    'start_time_1', 'finish_time_1',
                    'start_time_2', 'finish_time_2', )
    def constrains_period(self):
        for obj in self:

            beg_date = obj.begin_date.isocalendar()
            beg_day = beg_date[2]
            beg_week = beg_date[1]
            beg_year = beg_date[0]
            end_date = obj.end_date.isocalendar()
            end_day = end_date[2]
            end_week = end_date[1]
            end_year = end_date[0]

            if obj.begin_date > obj.end_date:
                raise exceptions.ValidationError(
                    _('Begin date must be less end date'))
            if obj.start_time_1 == 0 or obj.finish_time_1 == 0:
                raise exceptions.ValidationError(
                    _('Required Shift 1'))
            if obj.start_time_1 >= obj.finish_time_1:
                raise exceptions.ValidationError(
                    _('Start time must be less than finish'))
            if ((obj.schedule_shift == 'day' and
                 (beg_day != end_day or
                  (beg_week, beg_year) != (end_week, end_year))) or
                    (obj.schedule_shift == 'week' and
                     (beg_week, beg_year) != (end_week, end_year))):
                if obj.start_time_2 == 0 or obj.finish_time_2 == 0:
                    raise exceptions.ValidationError(
                        _('Required Shift 2'))
                if obj.start_time_2 >= obj.finish_time_2:
                    raise exceptions.ValidationError(
                        _('Start time must be less than finish'))
