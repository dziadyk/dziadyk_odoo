from odoo import fields, models, _


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'library Book Category'

    name = fields.Char()
    active = fields.Boolean(default=True, )
    book_count = fields.Integer(compute='_compute_book_count')

    def _compute_book_count(self):
        """Compute field book_count
        Count of books by search_count method

        :param None:
        :return None:
        """
        for rec in self:
            # Using search_count
            rec.book_count = self.env['library.book'].\
                search_count([('category_id', '=', rec.id)])

    def open_books_action(self):
        self.ensure_one()
        # Open list of books
        return {
            'name': _('Books'),
            'type': 'ir.actions.act_window',
            'view_type': 'list,form',
            'view_mode': 'list,form',
            'res_model': 'library.book',
            'target': 'current',
            'domain': [('category_id', '=', self.id)],
            'context': {'default_category_id': self.id},
        }
