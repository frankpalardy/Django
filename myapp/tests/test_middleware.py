# python
from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from myapp.middleware import MyCustomMiddleware

class MyCustomMiddlewareTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = MyCustomMiddleware(get_response=self.get_response)

    def get_response(self, request):
        return HttpResponse("Response")

    def test_middleware_process_request(self):
        request = self.factory.get('/some-path/')
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Response")

    def test_middleware_process_response(self):
        request = self.factory.get('/some-path/')
        response = self.middleware(request)
        # Add assertions to test the modifications made by the middleware
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Response", response.content)