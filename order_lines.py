from odoo import fields, models, api


class OrderLine(models.Model):
    _name = "toy_order.line"

    order_id = fields.Many2one(comodel_name="toy_order", string="Đơn đặt hàng")
    product_id = fields.Many2one(comodel_name="toy_product", string="Tên sản phẩm")
    description = fields.Char(string="Mô tả", related="product_id.description")
    sale_price = fields.Float(string="Đơn giá", related="product_id.price")
    amount = fields.Integer(string="Số lượng")
    sub_total = fields.Integer()



    @api.onchange('sale_price','amount')
    def onchange_qty_amount(self):
        if self.sale_price and self.amount:
            self.sub_total = self.sale_price * self.amount

    @api.onchange("amount","product_id")
    def total_quantity(self):
        if self.amount != 0 and self.order_id.state == "1":
            self.product_id.quantity = self.product_id.quantity - self.amount
