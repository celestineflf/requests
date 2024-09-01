from datetime import datetime, timedelta

from odoo import models, fields, api, _

class MainHub(models.Model):
    _name = "req.hub"
    _description = "Request Hub"
    _order = "sequence, id"

#fields

    name = fields.Char(string="Module Name", required=True,)
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=50)
    