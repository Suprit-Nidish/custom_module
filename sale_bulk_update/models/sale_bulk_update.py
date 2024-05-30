import datetime
from odoo import models, fields

class SaleBulkUpdate(models.Model):
    _inherit = 'sale.order'

    planned_days = fields.Char(string="Planned Days")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    def planned_dates_update(self):
        selected_ids = self.env.context.get('active_ids', [])
        selected_records = self.env['sale.order'].browse(selected_ids)
        for rec in selected_records:
            if not rec.planned_days:
                rec.start_date = datetime.date.today()
                rec.end_date = rec.start_date + datetime.timedelta(days=7)
                print(rec.end_date - rec.start_date)
                rec.planned_days = rec.end_date - rec.start_date
                print(self.planned_days, self.start_date, self.end_date)