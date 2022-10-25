from odoo import models, fields


class PatientChart(models.Model):
    _name = 'hr.hosp.patient.chart'
    _description = 'Patient chart'

    name = fields.Char()
    active = fields.Boolean(default=True)
    start_date = fields.Date()  # Необов'язково надавати ім'яб якщо воно співпадає з технічною назвою поля
    finish_date = fields.Date()  # Необов'язково надавати ім'яб якщо воно співпадає з технічною назвою поля
    diagnosis_ids = fields.Many2many(comodel_name='hr.hosp.diagnosis')
    description = fields.Char()
