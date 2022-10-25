{
    'name': "hr_hospital",
    'summary': 'Module for hospital',

    'author': "Dziadyk Volodymyr",
    'website': "https://oneservice-consulting.com",

    'category': 'Human Resources',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base'],  # Якщо модуль, не має прямих залежностей, він повінен мати залежність від базового модуля "base". Також це повинен бути список.

    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
        'views/patient_chart_views.xml',
    ],

}
