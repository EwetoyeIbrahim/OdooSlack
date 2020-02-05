# -*- coding: utf-8 -*-
import requests

from odoo import models, fields, api
from odoo.http import json, logging
from odoo.exceptions import Warning

# Initializing, the _logger object makes sure that the name of this file
# is carried along with the log messages.
_logger = logging.getLogger(__name__)

class OdooSlack(models.Model):
    _name = "odoo.slack"     
    name = fields.Char(string="Name", required=True)    
    description = fields.Text("Description")
    
    def slackup(self, slack_url, message):
        
        # Since this is just an extra module, most exceptions have to be handled
        # to enable other actions that may be in the pipeline to proceed
        error_msg = "Slack Notification won't be sent: "
        try:
            req = requests.post(
                slack_url, data=json.dumps(payload),
                headers={'Content-Type': 'application/json'}
            )
        except requests.exceptions.Timeout as e:
            _logger.warning(e)
            raise Warning(error_msg + 'Request Time-Out')
        except requests.exceptions.TooManyRedirects as e:
            _logger.warning(e)
            raise Warning(error_msg + 'Bad slack url as too many redirects were encountered')
        except requests.exceptions.RequestException as e:
            _logger.warning(e) 
            raise Warning(error_msg + "A dead end")
        except:
            _logger.warning(Exception) 
            raise Warning(error_msg + "An unkown error was encountered: May be Internet connection or something else")
        
        # Invalid slack URL will return 403 Error: Forbidden Client
        if req.status_code==403 :
            raise Warning(error_msg + "the Slack url is forbidden")