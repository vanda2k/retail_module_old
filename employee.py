# First code 10/11/2021 - Do Anh Van
from odoo import models, fields, api
from datetime import datetime


class Employee(models.Model):
    _name = "retail_staff"

    name = fields.Char(string="Họ Tên Nhân Viên", required=True)
    position_id = fields.Many2one(comodel_name="position", string="Chức Vụ")
    date_of_birth = fields.Date(string="Ngày Sinh")
    gender = fields.Selection(selection=[("1", "Nam"), ("2", "Nữ")], string="Giới Tính",required=True)
    cmnd = fields.Integer(string="CMND/CCCD")
    address = fields.Char(string="Địa Chỉ")
    phone = fields.Char(string="Số điện thoại")
    order_ids = fields.One2many(comodel_name="toy_order", inverse_name="employee_name_id")

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Employee, self).create(vals)
        return record
