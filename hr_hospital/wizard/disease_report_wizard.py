import datetime
from odoo import _, api, fields, models


class DiseaseReportWizard(models.TransientModel):
    _name = 'hr.hosp.disease.report.wizard'
    _description = 'Report Disease per month'

    year = fields.Integer(
        required=True, )
    month = fields.Selection(
        selection=[('1', 'January'),
                   ('2', 'February'),
                   ('3', 'March'),
                   ('4', 'April'),
                   ('5', 'May'),
                   ('6', 'June'),
                   ('7', 'July'),
                   ('8', 'August'),
                   ('9', 'September'),
                   ('10', 'October'),
                   ('11', 'November'),
                   ('12', 'December')],
        required=True, )
    disease_id = fields.Many2one(
        comodel_name='hr.hosp.disease',
        required=True, )
    count = fields.Integer(
        compute='_compute_count', )

    def action_open_wizard(self):
        return {
            'name': _('Report Disease per month'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hosp.disease.report.wizard',
            'target': 'new',
            'context': {'default_year': datetime.date.today().year,
                        'default_month': str(datetime.date.today().month)},
        }

    @api.depends('year', 'month', 'disease_id')
    def _compute_count(self):
        for rec in self:
            beg_date = datetime.datetime(rec.year, int(rec.month), 1)
            end_date = datetime.datetime(rec.year, int(rec.month)+1, 1)
            rec.count = self.env['hr.hosp.diagnosis'].search_count(
                [('disease_id', '=', rec.disease_id.id),
                 ('date', '>=', beg_date),
                 ('date', '<', end_date)])
