from odoo import exceptions, fields, models, _


class Status(models.Model):
    """Model for status, start and finish date
    In projects, requests and tasks
    """
    _name = 'task.tracker.status'
    _description = 'Status'
    _rec_name = 'status'

    active = fields.Boolean(
        default=True, )
    status = fields.Selection(
        selection=[('planed', _('Planned')),
                   ('in_work', _('In Work')),
                   ('completed', _('Completed')),
                   ('canceled', _('Canceled'))],
        required=True, default='planed', )
    cancellation_reason = fields.Text()
    start_date = fields.Date(
        required=True, )
    finish_date = fields.Date()

    def constrains_cancellation_reason(self):
        """Cancellation reason is a required field for status canceled

        :param None:
        :return None:
        """
        for rec in self:
            if rec.status == 'canceled' and not rec.cancellation_reason:
                raise exceptions.ValidationError(
                    _('Please fill in the cancellation reason'))
