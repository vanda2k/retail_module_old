from odoo import fields, models, api


class Supplier(models.Model):
    _name = "toy_supplier"

    name = fields.Char(string="Tên Nhà Cung Cấp")
    description = fields.Char(string="Mô tả")
    phone = fields.Char(string="Số điện thoại")
    supplier_ids = fields.One2many(comodel_name="purchase",inverse_name="supplier_id", string="Nhà cung cấp")