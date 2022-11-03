from odoo import _, api, exceptions, fields, models


class CreatePlanedVistWizard(models.TransientModel):
    _name = 'hr.hosp.create.planed.visit.wizard'
    _description = 'Create planed visit'

    planned_date = fields.Date(
        required=True, )
    planned_time = fields.Float(
        required=True, )
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', required=True, )
    patient_id = fields.Many2one(
        comodel_name='hr.hosp.patient', required=True, )

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

    def action_open_wizard(self):
        return {
            'name': _('Create planed visit'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hosp.create.planed.visit.wizard',
            'target': 'new',
            'context': {},
        }

    def action_create_record(self):
        self.ensure_one()
        self.env['hr.hosp.visit'].create({
            'planned_date': self.planned_date,
            'planned_time': self.planned_time,
            'doctor_id': self.doctor_id.id,
            'patient_id': self.patient_id.id,
        })
