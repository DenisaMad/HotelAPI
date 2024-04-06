import logging
from django.core.mail import mail_admins

class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger('error_logger')

    def __call__(self, request):
        
        response = self.get_response(request)
        if isinstance(response, Exception):
            self.processException(request, response)

        return response

    def processException(self, request, exception):
        error_message = f"Error: {exception}"
        
        self.logger.error(error_message)

        
        if isinstance(exception, Exception):  
            mail_admins('Critical Error Occurred', error_message)

        return None
