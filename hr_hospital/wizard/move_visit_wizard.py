from odoo import _, api, fields, models


class MoveVistWizard(models.TransientModel):
    _name = 'hr.hosp.move.visit.wizard'
    _description = 'Move visit'

    visit_id = fields.Many2one(
        comodel_name='hr.hosp.visit',
        domain=[('take_place', '=', False)],
        required=True, )
    patient_id = fields.Many2one(
        comodel_name='hr.hosp.patient',
        compute='_compute_visit_data',)
    old_doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor',
        compute='_compute_visit_data',
        string='Doctor', )
    old_planned_date = fields.Date(
        compute='_compute_visit_data',
        string='Date', )
    old_planned_time = fields.Float(
        compute='_compute_visit_data',
        string='Time', )
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor',
        required=True, )
    planned_date = fields.Date(
        required=True, )
    planned_time = fields.Float(
        required=True, )

    def action_open_wizard(self):
        return {
            'name': _('Move visit'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hosp.move.visit.wizard',
            'target': 'new',
            'context': {},
        }

    def action_create_record(self):
        self.ensure_one()
        self.env['hr.hosp.visit'].browse(self.visit_id.id).write({
            'doctor_id': self.doctor_id.id,
            'planned_date': self.planned_date,
            'planned_time': self.planned_time,
        })

    @api.depends('visit_id')
    def _compute_visit_data(self):
        for rec in self:
            rec.patient_id = rec.visit_id.patient_id
            rec.old_doctor_id = rec.visit_id.doctor_id
            rec.old_planned_date = rec.visit_id.planned_date
            rec.old_planned_time = rec.visit_id.planned_time
