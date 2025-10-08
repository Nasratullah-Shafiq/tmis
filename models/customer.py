from odoo import models, fields, api


class TailorCustomer(models.Model):
    _name = 'tailor.customer'


    _description = 'Tailor Customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Customer Name', required=True, tracking=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    note = fields.Text(string='Notes')
    image_1920 = fields.Image("Image")

    measurement_ids = fields.One2many('tailor.measurement', 'customer_id', string='Measurements')
    order_ids = fields.One2many('tailor.order', 'customer_id', string='Orders')


    def name_get(self):
        result = []

        for rec in self:
            display = rec.name
            if rec.phone:
                display = f"{rec.name} / {rec.phone}"
            result.append((rec.id, display))
            return result
