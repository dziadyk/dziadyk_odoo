from odoo import _, api, fields, models


class Diagnosis(models.Model):
    _name = 'hr.hosp.diagnosis'
    _description = 'Diagnosis'

    active = fields.Boolean(
        default=True, )
    date = fields.Datetime(
        required=True, )
    patient_id = fields.Many2one(
        comodel_name='hr.hosp.patient', required=True, )
    doctor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', required=True, )
    disease_id = fields.Many2one(
        comodel_name='hr.hosp.disease', )
    medical_test_ids = fields.Many2many(
        comodel_name='hr.hosp.medical.test', )
    treatment = fields.Text()
    is_intern = fields.Boolean(
        related="doctor_id.is_intern", )
    mentor_id = fields.Many2one(
        comodel_name='hr.hosp.doctor', related="doctor_id.mentor_id", )
    mentor_comment = fields.Text(
        string="Comment", )
    disease_type_id = fields.Many2one(
        comodel_name='hr.hosp.disease.type', string='Type',
        compute="_compute_disease_type",  store=True, )
    year = fields.Char(
        compute="_compute_period", store=True, )
    month = fields.Selection(
        selection=[('1', _('January')),
                   ('2', _('February')),
                   ('3', _('March')),
                   ('4', _('April')),
                   ('5', _('May')),
                   ('6', _('June')),
                   ('7', _('July')),
                   ('8', _('August')),
                   ('9', _('September')),
                   ('10', _('October')),
                   ('11', _('November')),
                   ('12', _('December'))],
        compute="_compute_period", store=True, )
    qty = fields.Integer(
        default=1, )

    def name_get(self):
        name_list = []
        for rec in self:
            name = "{} ({}) {}".format(
                rec.patient_id.name,
                rec.date,
                rec.disease_id.name, )
            name_list.append((rec.id, name))
        return name_list

    @api.depends('date')
    def _compute_period(self):
        for rec in self:
            rec.year = str(rec.date.year)
            rec.month = str(rec.date.month)

    @api.depends('disease_id')
    def _compute_disease_type(self):
        for rec in self:
            rec.disease_type_id = rec.disease_id.disease_type_id
