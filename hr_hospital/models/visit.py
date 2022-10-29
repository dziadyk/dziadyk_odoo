from odoo import _, api, exceptions, fields, models


class Visit(models.Model):
    _name = 'hr.hosp.visit'
    _description = 'Visit'
    _rec_name = 'patient_id'

    active = fields.Boolean(
        default=True, )
    planned_date = fields.Date()
    planned_time = fields.Float()
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
        for obj in self:
            exist_visits = self.env['hr.hosp.visit'].search_count(
                [('id', '!=', obj.id),
                 ('patient_id', '=', obj.patient_id.id),
                 ('planned_date', '=', obj.planned_date),
                 ('planned_time', '=', obj.planned_time)])
            if exist_visits:
                raise exceptions.ValidationError(
                    _('There is already a visit on this time'))

    @api.constrains('planned_date', 'reception_time',
                    'doctor_id', 'patient_id')
    def constrains_take_place(self):
        for obj in self:
            if obj.take_place:
                raise exceptions.ValidationError(
                    _('Visit has already taken place'))

    @api.constrains('active')
    def constrains_active(self):
        for obj in self:
            if not obj.active and obj.diagnosis_ids:
                raise exceptions.UserError(
                    _('Visit already has a diagnosis'))

    @api.ondelete(at_uninstall=False)
    def _unlink_only_empty_diagnosis(self):
        for obj in self:
            if obj.diagnosis_ids:
                raise exceptions.UserError(
                    _('Visit already has a diagnosis'))
