import datetime
from odoo import _, api, exceptions, fields, models


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(
        default=True, )
    birthday = fields.Date(
        string='Date of Birth', required=True, )
    age = fields.Integer(
        compute='_compute_age', )
    passport = fields.Char()
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', string='Personal Doctor', )
    emergency_contact_ids = fields.Many2many(
        comodel_name='hr.hosp.emergency.contact', )
    personal_doctor_ids = fields.One2many(
        comodel_name='hr.hosp.personal.doctor.history',
        inverse_name='patient_id', readonly=True, )
    diagnosis_ids = fields.One2many(
        comodel_name='hr.hosp.diagnosis',
        inverse_name='patient_id', readonly=True, )
    visit_count = fields.Integer(compute='_compute_depend_count')
    diagnosis_count = fields.Integer(compute='_compute_depend_count')
    test_count = fields.Integer(compute='_compute_depend_count')

    def write(self, vals):
        patient = super(Patient, self).write(vals)
        for rec in self:
            if 'doctor_id' in vals:
                doctor_history_dict = {
                    'patient_id': rec.id,
                    'doctor_id': vals['doctor_id'],
                    'datetime': datetime.datetime.now()}
                self.env['hr.hosp.personal.doctor.history'] \
                    .create(doctor_history_dict)
        return patient

    @api.constrains('birthday')
    def constrains_birthday(self):
        today = datetime.date.today()
        for rec in self:
            if rec.birthday > today:
                raise exceptions.ValidationError(
                    _('Birthday must be less than today'))

    @api.depends('birthday')
    def _compute_age(self):
        today = datetime.date.today()
        for rec in self:
            if rec.birthday:
                extra_year = ((today.month, today.day)
                              < (rec.birthday.month, rec.birthday.day))
                rec.age = today.year - rec.birthday.year - extra_year
            else:
                rec.age = 0

    @api.model
    def create(self, vals):
        patient = super(Patient, self).create(vals)
        if vals['doctor_id']:
            doctor_history_dict = {
                'patient_id': patient.id,
                'doctor_id': vals['doctor_id'],
                'datetime': datetime.datetime.now()
            }
            self.env['hr.hosp.personal.doctor.history'] \
                .create(doctor_history_dict)
        return patient

    def _compute_depend_count(self):
        for rec in self:
            rec.visit_count = self.env['hr.hosp.visit']. \
                search_count([('patient_id', '=', rec.id)])
            rec.diagnosis_count = self.env['hr.hosp.diagnosis']. \
                search_count([('patient_id', '=', rec.id)])
            rec.test_count = self.env['hr.hosp.medical.test']. \
                search_count([('patient_id', '=', rec.id)])

    def open_patient_visit_action(self):
        self.ensure_one()
        return {
            'name': _('Patient Visits'),
            'type': 'ir.actions.act_window',
            'view_type': 'list,form',
            'view_mode': 'list,form',
            'res_model': 'hr.hosp.visit',
            'target': 'current',
            'domain': [('patient_id', '=', self.id)],
            'context': {
                'default_patient_id': self.id,
                'default_doctor_id': self.doctor_id.id, },
        }

    def open_patient_diagnosis_action(self):
        self.ensure_one()
        return {
            'name': _('Patient Visits'),
            'type': 'ir.actions.act_window',
            'view_type': 'list,form',
            'view_mode': 'list,form',
            'res_model': 'hr.hosp.diagnosis',
            'target': 'current',
            'domain': [('patient_id', '=', self.id)],
            'context': {
                'default_patient_id': self.id,
                'default_doctor_id': self.doctor_id.id, },
        }

    def open_patient_medical_test_action(self):
        self.ensure_one()
        return {
            'name': _('Patient Visits'),
            'type': 'ir.actions.act_window',
            'view_type': 'list,form',
            'view_mode': 'list,form',
            'res_model': 'hr.hosp.medical.test',
            'target': 'current',
            'domain': [('patient_id', '=', self.id)],
            'context': {
                'default_patient_id': self.id,
                'default_doctor_id': self.doctor_id.id, },
        }

    def schedule_visit_action(self):
        self.ensure_one()
        return {
            'name': _('Create Planed Visit'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hr.hosp.create.planed.visit.wizard',
            'target': 'new',
            'domain': [],
            'context': {
                'default_patient_id': self.id,
                'default_doctor_id': self.doctor_id.id, },
        }

    def set_personal_doctor_action(self):

        id_list = []
        for rec in self:
            id_list.append(rec.id)

        return {
            'name': _('Set Personal Doctor'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hr.hosp.set.personal.doctor.multi.wizard',
            'target': 'new',
            'domain': [],
            'context': {
                'default_patient_ids': id_list, },
        }
