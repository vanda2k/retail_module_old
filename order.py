from odoo import models, fields, api
from datetime import datetime


class Order(models.Model):
    _name = "toy_order"

    def get_default_purchase_date(self):
        return datetime.now()

    number_order = fields.Char(string="Số Hoá Đơn", required=True)
    # customer_name_id = fields.Char(string="Ten Khach Hang")
    customer_name_id = fields.Many2one(comodel_name="toy_customer", string="Khách Hàng")
    # employee_name_id = fields.Char(string="Ten Nhan Vien")
    employee_name_id = fields.Many2one(comodel_name="retail_staff", string="Nhân Viên")
    oder_date = fields.Date(string="Ngày Tạo Hoá Đơn", default=get_default_purchase_date)
    total_price = fields.Float(string="Tổng tiền", compute="get_total_price")
    # Status viết sai
    status = fields.Selection(selection=[("0", "Tạo mới"), ("1", "Đã Thanh Toán"), ("2", "Huỷ bỏ")], string="Trạng thái")
    state = fields.Selection(selection=[("0", "Tạo mới"), ("1", "Đã Thanh Toán"), ("2", "Huỷ bỏ")], string="Trạng thái", default="0")

    order_line_ids = fields.One2many(comodel_name="toy_order.line",inverse_name="order_id", string="Đơn Hàng")

    # def new(self):
    #     self.state = "0"

    def success(self):
        self.state = "1"
    def cancel(self):
        self.state = "2"

    @api.onchange("toy_order.line.sub_total","total_price")
    def get_total_price(self):
        for order in self:
            total_price = 0
            for line in order.order_line_ids:
                total_price += line.sub_total
            order.total_price = total_price
