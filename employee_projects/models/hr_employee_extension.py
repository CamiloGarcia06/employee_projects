from odoo import models, fields, api


class HREmployee(models.Model):
    _inherit = "hr.employee"

    total_projects = fields.Integer(
        string="Total Projects", compute="_compute_total_projects", store=True
    )

    @api.depends("project_ids")
    def _compute_total_projects(self):
        for employee in self:
            employee.total_projects = len(employee.project_ids)

    project_ids = fields.One2many("employee.project", "employee_id", string="Projects")
