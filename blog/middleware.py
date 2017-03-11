"""
    blog.middleware
    ~~~~~~~~~~~~~~~

    middlewares for blog app.
"""

from django.http import HttpResponse, HttpResponseBadRequest
from .models import Host


class SetBloggerByHostMiddleware(object):
    """automatic set request ``blogger`` property according to request Host.

    **for example:**

    if the Host request-header field is _cosven.me_, then the middle set \
    ``request.blogger`` to 'cosven' according to a BloggerHostMap.

    a BloggerHostMap is predefined in :py:mod:`blog.consts`.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        hostname = request.META.get('HTTP_HOST')
        if hostname is None:
            return HttpResponseBadRequest('Request headers MUST have Host field.')

        try:
            host = Host.objects.get(name=hostname)
            request.blogger = host.user
        except Host.DoesNotExist:
            return HttpResponse('Request headers have an invalid Host field')

        # Code to be executed for each request/response after
        # the view is called.

        return self.get_response(request)
