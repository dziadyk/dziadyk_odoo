from odoo import _, fields, models


class DiseaseReportWizard(models.TransientModel):
    _name = 'hr.hosp.disease.report.wizard'
    _description = 'Report Disease per month'
    _rec_name = 'year'

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

    def action_open_wizard(self):
        return {
            'name': _('Report Disease per month'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hr.hosp.disease.report.wizard',
            'target': 'new',
            'context': {},
        }

    def action_get_report(self):
        self.ensure_one()
        #print('Year', self.year)
        #print('Month', self.month)
