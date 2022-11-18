{
    'name': "hr_hospital",
    'summary': 'Module for hospital',

    'author': "Dziadyk Volodymyr",
    'website': "https://oneservice-consulting.com",

    'category': 'Human Resources',
    'license': 'LGPL-3',
    'version': '15.0.1.0.0',

    'depends': [
        'base',
        "web",
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/doctor_schedule_views.xml',
        'views/visit_views.xml',
        'views/personal_doctor_history_views.xml',
        'views/emergency_contact_views.xml',
        'views/diagnosis_views.xml',
        'views/disease_type_views.xml',
        'views/disease_views.xml',
        'views/medical_test_type_views.xml',
        'views/medical_test_views.xml',
        'views/sample_type_views.xml',
        'views/specialty_views.xml',
        'wizard/set_personal_doctor_multi_wizard_views.xml',
        'wizard/disease_report_wizard_views.xml',
        'wizard/move_visit_wizard_views.xml',
        'wizard/create_planed_visit_wizard_views.xml',
        'wizard/doctor_schedule_wizard_views.xml',
        'report/doctor_report_templates.xml',
        'report/doctor_report_views.xml',
    ],

    'demo': [
        'data/emergency_contact_demo.xml',
        'data/specialty_demo.xml',
        'data/doctor_demo.xml',
        'data/patient_demo.xml',
        'data/disease_demo.xml',
        'data/medical_test_demo.xml',
        'data/diagnosis_demo.xml',
        'data/visit_demo.xml',
    ],

    'images': [
        'static/description/icon.png'
    ]

}
