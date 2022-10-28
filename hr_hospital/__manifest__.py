{
    'name': "hr_hospital",
    'summary': 'Module for hospital',

    'author': "Dziadyk Volodymyr",
    'website': "https://oneservice-consulting.com",

    'category': 'Human Resources',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': [
        'base',
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
    ],

    'images': [
        'static/description/icon.png'
    ]

}
