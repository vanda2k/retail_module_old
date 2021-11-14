# First code 10/11/2021 - Do Anh Van
from odoo import models, fields, api
from datetime import datetime

class Category(models.Model):
    _name = "toy_category"

    name = fields.Char(string="Loại mặt hàng")
    product_ids = fields.One2many(comodel_name="toy_product", inverse_name="category_id", string="Tên Sản Phẩm")
