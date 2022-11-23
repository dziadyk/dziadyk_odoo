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
            if not rec.member_ids:
                raise exceptions.ValidationError(
                    _('Team must have members'))

    @api.model
    def create(self, vals):
        team = super(Team, self).create(vals)
        for user_id in team.member_ids:
            self.env['res.users'].browse(user_id.id).write(
                {'team_id': team})
        return team

    def write(self, vals):
        team = super(Team, self).write(vals)
        for rec in self:
            if 'member_ids' in vals:
                for user_id in vals['member_ids'][0][2]:
                    self.env['res.users'].browse(user_id).write(
                        {'team_id': rec})
                users = self.env['res.users'].search([
                    ('team_id', '=', rec.id),
                    ('id', 'not in', vals['member_ids'][0][2])])
                for user in users:
                    self.env['res.users'].browse(user.id).write(
                        {'team_id': False})
        return team
