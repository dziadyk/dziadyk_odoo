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
        for rec in self:
            if rec.start_time >= rec.finish_time:
                raise exceptions.ValidationError(
                    _('Start time must be less than finish'))

            exist_schedule = self.env['hr.hosp.doctor.schedule'].search_count(
                [('id', '!=', rec.id),
                 ('date', '=', rec.date),
                 ('doctor_id', '=', rec.doctor_id.id),
                 '|', '|', '|',
                 '&',
                 ('start_time', '>', rec.start_time),
                 ('start_time', '<', rec.finish_time),
                 '&',
                 ('finish_time', '>', rec.start_time),
                 ('finish_time', '<', rec.finish_time),
                 '&',
                 ('start_time', '>=', rec.start_time),
                 ('finish_time', '<=', rec.finish_time),
                 '&',
                 ('start_time', '<=', rec.start_time),
                 ('finish_time', '>=', rec.finish_time)])
            if exist_schedule:
                error = 'Doctor already has a schedule at {}'.format(
                    rec.date)
                raise exceptions.ValidationError(_(error))
