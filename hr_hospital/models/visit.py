import datetime
import pytz
from odoo import _, api, exceptions, fields, models


class Visit(models.Model):
    _name = 'hr.hosp.visit'
    _description = 'Visit'
    _rec_name = 'patient_id'

    active = fields.Boolean(
        default=True, )
    planned_date = fields.Date()
    planned_time = fields.Float()
    visit_start = fields.Datetime(
        compute="_compute_visit_duration", store=True, )
    visit_stop = fields.Datetime(
        compute="_compute_visit_duration", store=True, )
    reception_time = fields.Datetime()
    take_place = fields.Boolean()
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', required=True, )
    patient_id = fields.Many2one(
        comodel_name='hr.hosp.patient', required=True, )
    diagnosis_ids = fields.Many2many(
        comodel_name='hr.hosp.diagnosis', )
    medical_test_ids = fields.Many2many(
        comodel_name='hr.hosp.medical.test', )
    recommendation = fields.Text()

    @api.constrains('planned_date', 'planned_time', 'patient_id')
    def constrains_planned_visit(self):
        for rec in self:
            exist_visits = self.env['hr.hosp.visit'].search_count(
                [('id', '!=', rec.id),
                 ('patient_id', '=', rec.patient_id.id),
                 ('planned_date', '=', rec.planned_date),
                 ('planned_time', '=', rec.planned_time)])
            if exist_visits:
                raise exceptions.ValidationError(
                    _('There is already a visit on this time'))

    @api.constrains('planned_date', 'reception_time',
                    'doctor_id', 'patient_id')
    def constrains_take_place(self):
        for rec in self:
            if rec.take_place:
                raise exceptions.ValidationError(
                    _('Visit has already taken place'))

    @api.constrains('active')
    def constrains_active(self):
        for rec in self:
            if not rec.active and rec.diagnosis_ids:
                raise exceptions.UserError(
                    _('Visit already has a diagnosis'))

    @api.depends('planned_date', 'planned_time')
    def _compute_visit_duration(self):
        for rec in self:

            minutes = rec.planned_time * 60
            h, m = divmod(minutes, 60)
            n_time = datetime.time(int(h), int(m))
            n_date = datetime.datetime.combine(rec.planned_date, n_time, )
            tz = pytz.timezone(self.env.user.tz or 'UTC')
            rec.visit_start = tz.localize(n_date).astimezone(pytz.utc)\
                .replace(tzinfo=None)

            minutes += 20
            h, m = divmod(minutes, 60)
            n_time = datetime.time(int(h), int(m))
            n_date = datetime.datetime.combine(rec.planned_date, n_time, )
            tz = pytz.timezone(self.env.user.tz or 'UTC')
            rec.visit_stop = tz.localize(n_date).astimezone(pytz.utc) \
                .replace(tzinfo=None)

    @api.ondelete(at_uninstall=False)
    def _unlink_only_empty_diagnosis(self):
        for rec in self:
            if rec.diagnosis_ids:
                raise exceptions.UserError(
                    _('Visit already has a diagnosis'))

    @api.model
    def create(self, vals):
        if vals['planned_date'] \
                and vals['planned_date'] < datetime.date.today():
            raise exceptions.UserError(
                _('Planed date must be greater than today'))
        visit = super(Visit, self).create(vals)
        return visit

    def name_get(self):
        name_list = []
        for rec in self:
            visit_name = rec.patient_id.name
            if rec.planned_date:

                minutes = rec.planned_time * 60
                hours, minutes = divmod(minutes, 60)

                visit_name += " ({} {}) {}".format(
                    rec.planned_date,
                    "%02d:%02d" % (hours, minutes),
                    rec.doctor_id.name, )
            else:
                visit_name += " ({}) {}".format(
                    rec.reception_time,
                    rec.doctor_id.name, )
            name_list.append((rec.id, visit_name))
        return name_list

    def move_visit_action(self):
        self.ensure_one()
        return {
            'name': _('Move Visit'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hr.hosp.move.visit.wizard',
            'target': 'new',
            'domain': [],
            'context': {
                'default_visit_id': self.id, },
        }
