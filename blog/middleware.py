"""
    blog.middleware
    ~~~~~~~~~~~~~~~

    middlewares for blog app.
"""

from django.http import HttpResponse, HttpResponseBadRequest
from .consts import BloggerHostMap


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

        host = request.META.get('HTTP_HOST')
        if host is None:
            return HttpResponseBadRequest('Host not allowed.')

        for blogger, hosts in BloggerHostMap.items():
            if host in hosts:
                request.blogger = blogger.value
                break
        else:
            return HttpResponse('Invalid Host header: %s.' % host)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
