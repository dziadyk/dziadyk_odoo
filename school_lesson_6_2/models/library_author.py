import datetime
from odoo import api, fields, models


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Authors'

    first_name = fields.Char(required=True, translate=True)
    last_name = fields.Char(required=True, translate=True)
    birth_date = fields.Date('Birthday')
    trainee_access = fields.Boolean(compute='_compute_trainee_access',)

    @api.depends('create_date')
    def _compute_trainee_access(self):
        for rec in self:
            if (rec.create_date >
                    datetime.datetime.now() + datetime.timedelta(days=-30)):
                rec.trainee_access = True
            else:
                rec.trainee_access = False

    def name_get(self):
        return [(rec.id, "%s %s" % (
            rec.first_name, rec.last_name)) for rec in self]

    def action_delete(self):
        self.ensure_one()
        self.check_access_rights('unlink')
        self.unlink()

    def _create_by_user(self, vals):
        return self.sudo().create(vals)
