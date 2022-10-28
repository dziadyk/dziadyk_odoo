from odoo import api, exceptions, fields, models, _


class MedicalTestType(models.Model):
    _name = 'hr.hosp.medical.test.type'
    _description = 'Medical Test Type'
    _parent_name = 'parent_id'
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(
        required=True, )
    active = fields.Boolean(
        default=True, )
    complete_name = fields.Char(
        compute='_compute_complete_name',
        recurcive=True, store=True, )
    parent_id = fields.Many2one(
        comodel_name='hr.hosp.medical.test.type',
        string='Disease Type', ondelete='cascade')
    parent_path = fields.Char()

    @api.constrains('parent_id')
    def _check_type_recursion(self):
        if not self._check_recursion():
            raise exceptions.ValidationError(
                _('You cannot create recursive types'))

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for obj in self:
            if obj.parent_id:
                obj.complete_name = '%s / %s' \
                                    % (obj.parent_id.complete_name, obj.name)
            else:
                obj.complete_name = obj.name
