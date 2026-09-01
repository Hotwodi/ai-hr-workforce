{
    'name': 'AI HR Workforce Management & Attendance Fraud Detection',
    'version': '18.0.1.0.0',
    'images': ['static/description/cover.png'],
    'category': 'Productivity/AI',
    'summary': 'Detect attendance anomalies and manage workforce compliance with AI.',
    'description': '''
        HR workforce management with AI attendance analysis, fraud detection, scheduling, and compliance dashboards.
        =====================================================
        Detect attendance anomalies and manage workforce compliance with AI.
    ''',
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 129.0,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/ai_hr_workforce_v2_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
