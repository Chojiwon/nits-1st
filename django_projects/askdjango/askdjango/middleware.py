from types import GeneratorType
from django.db.models import Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from askdjango.encoders import CustomDjangoJSONEncoder


class JsonResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if isinstance(response, str):
            if response and response[0] in ('"', '[', '{'):
                return HttpResponse(response, content_type='application/json')
            return HttpResponse(response)
        elif isinstance(response, (set, dict, list, tuple, QuerySet, Model)):
            return JsonResponse(response, encoder=CustomDjangoJSONEncoder, json_dumps_params={'ensure_ascii': False, 'indent': 2}, safe=False)
        else:
            return response

