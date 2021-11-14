# First code 10/11/2021 - Do Anh Van
from odoo import models, fields, api
from datetime import datetime

class Product(models.Model):
    _name = "toy_product"

    def get_default_purchase_date(self):
        return datetime.now()

    # Cac truong
    product_ids = fields.One2many(comodel_name="purchase", inverse_name="product_id")
    name = fields.Char(string="Tên Mặt Hàng", required=True)
    unit_id = fields.Many2one(comodel_name="toy_unit", string="Đơn Vị Tính")
    category_id = fields.Many2one(comodel_name="toy_category", string="Loại Mặt Hàng")
    purchase_order_id = fields.Many2one(commodel_name="purchase_order", string="Đơn đặt hàng")


    purchase = fields.Float(string="Giá Mua")
    price = fields.Float(string="Giá Bán")
    expiry_date = fields.Datetime(string="Hạn Sử Dụng")
    date_of_manufacture = fields.Datetime(string="Ngày sản xuất")
    barcode = fields.Integer(string="Mã Vạch")
    description = fields.Char(string="Mô Tả")
    quantity = fields.Integer(string="Số Lượng")


    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Product, self).create(vals)
        return record

