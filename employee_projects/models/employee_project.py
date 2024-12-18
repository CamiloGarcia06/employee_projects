from odoo import models, fields


class EmployeeProject(models.Model):
    _name = "employee.project"
    _description = "Employee Project"

    name = fields.Char(string="Project Name", required=True)
    description = fields.Text(string="Project Description")
    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
