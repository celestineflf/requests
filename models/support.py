from datetime import datetime, timedelta

from odoo import models, fields, api, _, _lt
from odoo.exceptions import ValidationError, UserError
from odoo.osv import expression
from odoo.osv.query import Query

class SpTicket(models.Model):
    _name = "req.sp.ticket"
    _inherit = "mail.thread", "mail.activity.mixin", 
    _description = "Support Tickets"


#Fields

    name = fields.Char(string="Support Reference")
    short_desc = fields.Char(string="Short Description")
    state = fields.Selection([
        ('cancel', 'Cancelled'),
        ('new', 'New'),
        ('sent', 'Sent'),
        ('approve', 'Approved'),
        ('pending', 'In Progress'),
        ('done', 'Done'),
        ], string="status", readonly=True, copy=False, index=True, default='new')
    is_urgent = fields.Boolean(string="Urgent")
    type = fields.Selection([
        ('new', 'New Device'),
        ('update', 'Update System'),
        ('error', 'Error Solve'),
        ('clean', 'Cleanup'),
        ('bug', 'Node-Red'),
        ], string="Ticket Type", readonly=False, copy=False, index=True, default='new')
    date_sent = fields.Date(string="Date Sent", required=False, readonly=True, index=True, copy=False,)
    date_approve = fields.Date(string="Date Approved")
    date_end = fields.Date(string="Date Finished")
    duration = fields.Float(string="Time Spent")
    user_id = fields.Many2one(
        'res.users', string="Responsible User", index=True, default=lambda self: self.env.user,
        domain=lambda self: "[('share', '=', False)]".format(
            self.env.user
        ),)
    meet_users = fields.Many2many(
        'res.users', string="Meeting Participants", index=True, domain=lambda self: "[('share', '=', False)]".format(
            self.env.user
        ),)
    description = fields.Html(string="Support Ticket Details")
    progress = fields.Float(string="Progress")
    date_meeting = fields.Date(string="Appointment Date")
    meeting_desc = fields.Char(string="Appointment Description")
    meet_time = fields.Float(string="Appointment Time")
    partner_id = fields.Many2one(
       'res.partner', string="Customer", index=True, readonly=True, default=lambda self: self.order_id.partner_id, 
    )
    order_id = fields.Many2one(
        'sale.order', string="Sales Order", copy=False, store=True, index=True, readonly=False, domain="[]"
    )

    
    
    
    


#Create Sequence

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('req.sp.ticket')
        return super(SpTicket, self).create(vals)



#Button Actions for  Ticket Form View

    def action_ticket_send(self):
        self['state'] = 'sent'
        self['date_sent'] = fields.Datetime.today()

    def action_ticket_approve(self):
        self['state'] = 'approve'
        self['date_approve'] = fields.Datetime.today()

    def action_ticket_cancel(self):
        self['state'] = 'cancel'

    def action_ticket_reset(self):
        self['state'] = 'new'

    def action_ticket_done(self):
        self['state'] = 'done'
        self['date_end'] = fields.Datetime.today()


#onchange

    @api.onchange('order_id')
    def onchange_order_id(self):
        if self.order_id != False:
            self.partner_id = self.order_id.partner_id
        



#Action send notification to user_id
    
    
    

    

