# python
from django.utils.deprecation import MiddlewareMixin

class MyCustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Add custom request processing here
        pass

    def process_response(self, request, response):
        # Add custom response processing here
        return response