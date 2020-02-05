# -*- coding: utf-8 -*-
{
    'name': "Odoo-Slack",

    'summary': """
        Odoo to Slack Notification integration
        """,

    'description': 
        """
        This module simply accepts message, and slack Id to perform hand-shakes between odoo and slack.
        Kindly note that: requests library, which as of now, is not shipped with python has to be installed on the system.
        pip install requests
        """,

    'author': "Ewetoye, Ibrahim",
    'website': "https://github.com/EwetoyeIbrahim/Odoo-Slack",

    
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

}