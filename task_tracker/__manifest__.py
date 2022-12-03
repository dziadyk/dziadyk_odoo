# Copyright © 2022 Oneservice (<https://www.oneservice-consulting.com>)
# @author: Volodymyr Dziadyk (<dvol@oneservice.in.ua>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

{
    'name': 'Task Tracker',
    'version': '15.0.1.0.0',
    'category': 'Services',
    'summary': """Task Tracker""",
    'license': 'LGPL-3',
    'author': 'Volodymyr Dziadyk',
    'website': 'https://www.oneservice-consulting.com',

    'depends': [
        'base',
    ],

    'data': [
        'security/task_tracker_groups.xml',
        'security/task_tracker_security.xml',
        'security/ir.model.access.csv',
        'views/task_tracker_menus.xml',
        'views/project_views.xml',
        'views/request_views.xml',
        'views/task_views.xml',
        'views/timesheet_views.xml',
        'views/team_views.xml',
        'report/project_report_templates.xml',
        'report/project_report_views.xml',
    ],

    'demo': [
        'data/task_tracker_team_demo.xml',
        'data/task_tracker_project_demo.xml',
        'data/task_tracker_request_demo.xml',
        'data/task_tracker_task_demo.xml',
        'data/task_tracker_timesheet_demo.xml',
    ],

    'support': 'dvol@oneservice.in.ua',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
