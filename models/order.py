from odoo import models, fields, api


class TailorOrder(models.Model):
    _name = 'tailor.order'
    _description = 'Tailor Order'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: 'New')
    customer_id = fields.Many2one('tailor.customer', string='Customer', required=True)
    measurement_id = fields.Many2one('tailor.measurement', string='Measurement')
    order_line_ids = fields.One2many('tailor.order.line', 'order_id', string='Order Lines')

    tailor_id = fields.Many2one('res.users', string='Assigned Tailor')
    date_order = fields.Date(string='Order Date', default=fields.Date.context_today)
    delivery_date = fields.Date(string='Delivery Date')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    total_amount = fields.Monetary(string='Total', compute='_compute_total', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    note = fields.Text(string='Notes')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            seq = self.env['ir.sequence'].next_by_code('tailor.order.seq') or 'TORDER/0001'
            vals['name'] = seq
            return super().create(vals)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_start(self):

        for rec in self:
            rec.state = 'in_progress'

    def action_done(self):

        for rec in self:
            rec.state = 'done'

    def action_cancel(self):

        for rec in self:
            rec.state = 'cancel'

    @api.depends('order_line_ids.price_subtotal')
    def _compute_total(self):

        for rec in self:
            rec.total_amount = sum(rec.order_line_ids.mapped('price_subtotal'))

class TailorOrderLine(models.Model):

    _name = 'tailor.order.line'
    _description = 'Tailor Order Line'

    order_id = fields.Many2one('tailor.order', string='Order', ondelete='cascade')
    name = fields.Char(string='Description')
    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string='Quantity', default=1.0)
    price_unit = fields.Float(string='Unit Price')
    price_subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('qty', 'price_unit')
    def _compute_subtotal(self):
        for ln in self:
            ln.price_subtotal = ln.qty * ln.price_unit
