from odoo import models, fields, api
from datetime import datetime


class Customer(models.Model):
    _name = "toy_customer"

    name = fields.Char(string="Ten Khach Hang", required=True)
    iscustomer = fields.Boolean(string="Khách Hàng", default=True)
    issupplier = fields.Boolean(string="Nhà Cung Cấp", default=True)
    company = fields.Char(string="Ten cong ty")
    address = fields.Char(string="Dia chi")
    phone = fields.Char(string="So dien thoai")
    order_ids = fields.One2many(comodel_name="toy_order", inverse_name="customer_name_id")
    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Customer, self).create(vals)
        return record