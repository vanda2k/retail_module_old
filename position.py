# First code 10/11/2021 - Do Anh Van
from odoo import models, fields, api

class Position(models.Model):
    _name = "position"

    name = fields.Char(string="Tên Chức Vụ",required=True)
    employee_ids = fields.One2many(comodel_name="retail_staff", inverse_name="position_id", string="Tên Nhân Viên")
    # employee_ids = fields.Char(string="Chức Vụ")

    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].title()
        record = super(Position, self).create(vals)
        return record