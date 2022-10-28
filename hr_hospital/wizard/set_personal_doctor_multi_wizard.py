from odoo import _, fields, models


class SetPersonalDoctorMultiWizard(models.TransientModel):
    _name = 'hr.hosp.set.personal.doctor.multi.wizard'
    _description = 'Wizard to set personal doctor'
    _rec_name = 'doctor_id'

    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor',
        string='Personal Doctor', required=True, )
    patient_ids = fields.Many2many(
        comodel_name='hr.hosp.patient', string='Patients', )

    def action_open_wizard(self):
        return {
            'name': _('Set Personal Doctor Wizard'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hosp.set.personal.doctor.multi.wizard',
            'target': 'new',
            'context': {},
        }

    def action_create_record(self):
        self.ensure_one()
        for patient in self.patient_ids:
            if patient.doctor_id != self.doctor_id:
                self.env['hr.hosp.patient'].browse(patient.id).write({
                    'doctor_id': self.doctor_id.id,
                })
