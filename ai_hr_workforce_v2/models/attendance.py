from odoo import models, fields


class Attendance(models.Model):
    _name = 'ai.hr.attendance'
    _description = 'AI HR Attendance Alert'
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    note = fields.Text(string='Notes')
