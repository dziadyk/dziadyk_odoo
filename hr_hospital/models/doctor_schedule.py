from odoo import _, api, exceptions, fields, models


class DoctorSchedule(models.Model):
    _name = 'hr.hosp.doctor.schedule'
    _description = 'Doctor Schedule'
    _rec_name = 'doctor_id'

    active = fields.Boolean(
        default=True, )
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', )
    date = fields.Date()
    start_time = fields.Float()
    finish_time = fields.Float()

    @api.constrains('start_time', 'finish_time')
    def constrains_work_time(self):
        for obj in self:
            if obj.start_time >= obj.finish_time:
                raise exceptions.ValidationError(
                    _('Start time must be less than finish'))

            exist_schedule = self.env['hr.hosp.doctor.schedule'].search_count(
                [('id', '!=', obj.id),
                 ('date', '=', obj.date),
                 ('doctor_id', '=', obj.doctor_id.id),
                 '|',
                 '&',
                 ('start_time', '>', obj.start_time),
                 ('start_time', '<', obj.finish_time),
                 '&',
                 ('finish_time', '>', obj.start_time),
                 ('finish_time', '<', obj.finish_time)])
            if exist_schedule:
                raise exceptions.ValidationError(
                    _('Doctor already has a schedule on this time'))
