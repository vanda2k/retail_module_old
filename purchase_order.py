from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _name = "purchase_order"

    purchase_id = fields.Many2one(comodel_name="purchase", string="Đơn hàng nhập")
    product_id = fields.Many2one(comodel_name="toy_product", string="Tên sản phẩm")
    description = fields.Char(string="Mô tả", related="product_id.description")
    purchase_price = fields.Float(string="Đơn giá", related="product_id.purchase")
    sub_total = fields.Integer(string="Tổng tiền nhập")
    purchase_order_ids = fields.One2many(comodel_name="toy_product", inverse_name="purchase_order_id")
    purchase_amount = fields.Integer(string="Số lượng hiện có", related="product_id.quantity")
    purchase_quantity = fields.Integer(string="Số lượng nhập")

    @api.onchange("purchase_quantity","product_id")
    def total_quantity(self):
        if self.product_id.quantity == 0 or self.product_id.quantity != 0:
            self.product_id.quantity = self.purchase_quantity + self.product_id.quantity
            print(self.purchase_quantity)

    @api.onchange("purchase_quantity","product_id.purchase")
    def onchange_sub_total_purchase(self):
        if self.purchase_quantity != 0:
            self.sub_total = self.purchase_quantity * self.product_id.purchase