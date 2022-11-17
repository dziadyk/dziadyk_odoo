from odoo import fields, models


class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'library Book Category'

    name = fields.Char()
    active = fields.Boolean(default=True, )
