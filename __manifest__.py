# -*- coding: utf-8 -*-
{
    'name': 'OdooSlack',

    'summary': 'Odoo to Slack Notification integration',

    'description': 
        '''
        This module simply accepts message, and slack Id to perform hand-shakes between odoo and slack.
        Kindly note that: requests library, which as of now, is not shipped with python has to be installed on the system.
        pip install requests
        ''',

    'author': 'Medsaf.com, Ewetoye Ibrahim',
    
    'website': 'https://github.com/EwetoyeIbrahim/OdooSlack',

    'external_dependencies': {'python': ['requests']},
    
    'category': 'Extra Tools',
    
    'version': '0.1',

    'depends': ['base'],
}