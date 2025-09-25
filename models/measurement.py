from odoo import models, fields, api


class TailorMeasurement(models.Model):

    _name = 'tailor.measurement'
    _description = 'Tailor Measurement'

    name = fields.Char(string='Measurement Name', help='e.g. "Shirt - Standard"', required=True)
    customer_id = fields.Many2one('tailor.customer', string='Customer', ondelete='cascade', required=True)
    clothing_type = fields.Selection([
        ('shirt', 'Shirt'),
        ('pant', 'Pant'),
        ('suit', 'Suit'),
        ('dress', 'Dress'),
        ('other', 'Other')
    ], string='Clothing Type', default='shirt')

    # example measurement fields (extendable)
    chest = fields.Float(string='Chest (cm)')
    waist = fields.Float(string='Waist (cm)')
    hip = fields.Float(string='Hip (cm)')
    shoulder = fields.Float(string='Shoulder (cm)')
    sleeve = fields.Float(string='Sleeve Length (cm)')
    length = fields.Float(string='Length (cm)')

    active = fields.Boolean(default=True)
    note = fields.Text(string='Notes')