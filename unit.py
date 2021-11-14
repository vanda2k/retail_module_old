# First code 10/11/2021 - Do Anh Van
from odoo import models, fields, api

class Unit(models.Model):
    _name = "toy_unit"

    name = fields.Char(string="Tên Đơn Vị")
    product_ids = fields.One2many(comodel_name="toy_product", inverse_name="unit_id", string="Tên Sản Phẩm")