from odoo import api, exceptions, fields, models, _


class Doctor(models.Model):
    _name = 'hr.hosp.doctor'
    _description = 'Doctor'
    _inherit = 'hr.hosp.person'

    active = fields.Boolean(
        default=True, )
    specialty = fields.Char()
    is_intern = fields.Boolean(
        string='Intern', )
    mentor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor',
        domain=[('is_intern', '=', False)], )

    @api.constrains('is_intern', 'mentor_id')
    def constrains_intern_mentor(self):
        for obj in self:
            if obj.is_intern and not obj.mentor_id:
                raise exceptions.ValidationError(
                    _('Intern must must have a mentor'))

    @api.onchange('is_intern')
    def onchange_is_intern(self):
        for obj in self:
            if obj.mentor_id:
                obj.mentor_id = 0
