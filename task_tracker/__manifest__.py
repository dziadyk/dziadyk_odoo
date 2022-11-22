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
        'security/ir.model.access.csv',
        'views/task_tracker_menus.xml',
        'views/project_views.xml',
        'views/request_views.xml',
        'views/task_views.xml',
        'views/team_views.xml',
    ],

    'support': 'dvol@oneservice.in.ua',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
