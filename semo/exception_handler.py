from django.http import JsonResponse
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    if isinstance(exc, ValidationError):
        data = {}
        data['errors'] = dict(exc.detail)
        data['detail'] = 'json or query param validation error'
        return JsonResponse(data, status=400)
    return exception_handler(exc, context)
