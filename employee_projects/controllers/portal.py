from odoo import http
from odoo.http import request


class EmployeeProjectPortal(http.Controller):

    @http.route(["/my/projects"], type="http", auth="public", website=True)
    def portal_my_projects(self, **kw):
        employee = request.env.user.employee_id
        projects = request.env["employee.project"].sudo().search(
            []
        )
        return request.render(
            "employee_projects.portal_my_projects",
            {
                "projects": projects,
            },
        )

    @http.route(
        ["/my/projects/<int:project_id>"], type="http", auth="public", website=True
    )
    def portal_project_detail(self, project_id, **kw):
        project = request.env["employee.project"].browse(project_id)
        return request.render(
            "employee_projects.portal_project_detail",
            {
                "project": project,
            },
        )
