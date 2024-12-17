{
    'name': 'Employee Projects',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Manage employee projects',
    'depends': ['base', 'hr', 'portal', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_project_views.xml',
        'views/hr_employee_views.xml',
        'views/portal_templates.xml',
    ],
    'installable': True,
    'application': True,
}