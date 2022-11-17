import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(
        translate=True, required=True, )
    book_description = fields.Text(
        string='Text', translate=True, )
    author_id = fields.Many2one(
        comodel_name='author.of.book', index=True, ondelete='cascade')
    additional_text = fields.Text(
        translate=True, )

    def set_confirm(self):
        pass


class AuthorOfBook(models.Model):
    _name = 'author.of.book'
    _description = 'Author of book'

    name = fields.Char(
        translate=True, required=True, )
    last_name = fields.Char(
        translate=True, )
    biography_text = fields.Text(
        string='Text', translate=True, )
    book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name='author_id',
        string='Books', )
    color = fields.Integer()

    def set_confirm(self):
        pass

    def get_full_name(self):
        self.ensure_one()
        return f'{self.name} {self.last_name}'
