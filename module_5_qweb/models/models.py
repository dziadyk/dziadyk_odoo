import logging

from odoo import models, fields, _

_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(
        string=_('Name'),
        translate=True,
        required=True, )
    book_description = fields.Text(
        string=_('Text'),
        translate=True, )
    author_id = fields.Many2one(
        comodel_name='author.of.book',
        string=_('Author'), index=True, ondelete='cascade')
    additional_text = fields.Text(
        string=_('Additional Text'),
        translate=True, )

    def set_confirm(self):
        pass


class AuthorOfBook(models.Model):
    _name = 'author.of.book'
    _description = 'Author of book'

    name = fields.Char(
        string=_('Name'),
        translate=True,
        required=True, )
    last_name = fields.Char(
        string=_('Last Name'),
        translate=True, )
    biography_text = fields.Text(
        string=_('Text'),
        translate=True, )
    book_ids = fields.One2many(
        comodel_name='library.book',
        inverse_name='author_id',
        string=_('Books'), )
    color = fields.Integer(
        string=_('Color'), )

    def set_confirm(self):
        pass

    def get_full_name(self):
        self.ensure_one()
        return f'{self.name} {self.last_name}'
