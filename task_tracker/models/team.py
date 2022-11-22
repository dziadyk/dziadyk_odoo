from odoo import api, exceptions, fields, models, _


class Team(models.Model):
    _name = 'task.tracker.team'
    _description = 'Team'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    member_ids = fields.Many2many(
        comodel_name='res.users',
        string='Members', )
    lead_id = fields.Many2one(
        comodel_name='res.users',
        string='Team Lead',
        required=True, )

    @api.constrains('member_ids', 'lead_id')
    def constrains_lead_is_member(self):
        for rec in self:
            if not(rec.lead_id in rec.member_ids):
                raise exceptions.ValidationError(
                    _('Lead must be a member of team'))
