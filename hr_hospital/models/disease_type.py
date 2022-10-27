from odoo import api, exceptions, fields, models, _


class DiseaseType(models.Model):
    _name = 'hr.hosp.disease.type'
    _description = 'Disease Type'
    _parent_name = 'parent_id'
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(required=True)
    complete_name = fields.Char(compute='_compute_complete_name', recurcive=True, store=True)
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('hr.hosp.disease.type', string='Disease Type', ondelete='cascade')
    parent_path = fields.Char()

    @api.depends ('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for type in self:
            if type.parent_id:
                type.complete_name = '%s / %s' % (type.parent_id.complete_name, type.name)
            else:
                type.complete_name = type.name

    @api.constrains('parent_id')
    def _check_type_recursion(self):
        if not self._check_recursion():
            raise exceptions.ValidationError(_('You cannot create recursive types'))
