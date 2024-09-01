from datetime import datetime, timedelta

from odoo import models, fields, api, _

class ItTicket(models.Model):
    _name = "req.it.ticket"
    _inherit = "mail.thread", "mail.activity.mixin"
    _description = "IT Tickets"


#Fields

    name = fields.Char(string="Ticket Reference")
    short_desc = fields.Char(string="Short Description")
    state = fields.Selection([
        ('cancel', 'Cancelled'),
        ('new', 'New'),
        ('sent', 'Sent for Development'),
        ('approve', 'Approved'),
        ('pending', 'In Progress'),
        ('done', 'Done'),
        ], string="status", readonly=True, copy=False, index=True, default='new')
    is_urgent = fields.Boolean(string="Urgent")
    type = fields.Selection([
        ('new', 'New Development'),
        ('update', 'Update Existing'),
        ('error', 'Error Solve'),
        ('clean', 'UI Cleanup'),
        ('bug', 'Bug Fix'),
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
    description = fields.Html(string="Ticket Details")
    progress = fields.Float(string="Progress")
    date_meeting = fields.Date(string="Appointment Date")
    meeting_desc = fields.Char(string="Appointment Description")
    meet_time = fields.Float(string="Appointment Time")
    
    
    
    


#Create Sequence

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('req.it.ticket')
        return super(ItTicket, self).create(vals)



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
        
    def action_ticket_pending(self):
        self['state'] = 'pending'


#Action send notification to user_id
    
    
    

    

