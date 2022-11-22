from odoo import api, fields, models


class Request(models.Model):
    _name = 'task.tracker.request'
    _inherit = 'task.tracker.status'
    _description = 'Request'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    project_id = fields.Many2one(
        comodel_name='task.tracker.project',
        required=True, )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        compute='_compute_partner_id', )
    description = fields.Text()

    @api.depends('project_id')
    def _compute_partner_id(self):
        for rec in self:
            rec.partner_id = rec.project_id.partner_id
