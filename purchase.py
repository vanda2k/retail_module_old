from odoo import fields, models, api
from datetime import datetime


class Purchase(models.Model):
    _name = "purchase"

    def get_default_purchase_date(self):
        return datetime.now()

    number_purchase = fields.Char(string="Ten phieu nhap")
    state = fields.Selection(selection=[
        ("0", "Đặt hàng"),
        ("1", "Đang di chuyển"),
        ("2", "Hoàn thành"),
        ("3", "Huỷ bỏ")],
        string="Trạng thái", default="0")
    supplier_id = fields.Many2one(comodel_name="toy_supplier", string="Tên nhà cung cấp")
    # Ngay tao hoa don
    purchase_date = fields.Date(string="Ngày Tạo Hoá Đơn", default=get_default_purchase_date)
    employee_id = fields.Many2one(comodel_name="retail_staff", string="Nhân viên nhập hàng")
    product_id = fields.Char(string="id")
    # product_name = fields.Char(string="Tên sản phẩm", related="product_id.name")
    amount = fields.Integer(string="Số lượng nhập")
    purchase_order_ids = fields.One2many(comodel_name="purchase_order",inverse_name="purchase_id", string="Đơn Hàng Nhập")
    total_purchase = fields.Float(string="Tổng tiền")

    def move(self):
        self.state = "1"

    def cancel(self):
        self.state = "3"

    def success(self):
        self.state = "2"

    # @api.onchange("purchase_order_ids.sub_total")
    def get_total_purchase(self):
        for order in self:
            total = 0
            for line in order.purchase_order_ids:
                total += line.sub_total
            order.total_purchase = total


