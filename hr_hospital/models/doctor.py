from odoo import _, api, exceptions, fields, models


class Doctor(models.Model):
    _name = 'hr.hosp.doctor'
    _description = 'Doctor'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(
        default=True, )
    specialty_id = fields.Many2one(
        comodel_name='hr.hosp.specialty',
        required=True, )
    is_intern = fields.Boolean(
        string='Intern', )
    mentor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor',
        domain=[('is_intern', '=', False)],
        ondelete='cascade', )
    intern_ids = fields.One2many(
        comodel_name='hr.hosp.doctor',
        inverse_name='mentor_id', )
    patient_ids = fields.One2many(
        comodel_name='hr.hosp.patient',
        inverse_name='doctor_id', readonly=True, )

    @api.constrains('is_intern', 'mentor_id')
    def constrains_intern_mentor(self):
        for rec in self:
            if rec.is_intern and (not rec.mentor_id
                                  or rec.mentor_id.id == rec.id):
                raise exceptions.ValidationError(
                    _('Intern must must have a mentor'))

    @api.onchange('is_intern')
    def onchange_is_intern(self):
        for rec in self:
            if not rec.is_intern and rec.mentor_id:
                rec.mentor_id = 0

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
                'default_doctor_id': self.id, },
        }
