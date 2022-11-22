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
        compute='_compute_project_data', )
    description = fields.Text()

    def _compute_project_data(self):
        for rec in self:
            rec.partner_id = rec.project_id.partner_id

    @api.onchange('project_id')
    def _onchange_project_id(self):
        self.partner_id = self.project_id.partner_id
