from django.http import HttpResponse, HttpResponseBadRequest
from .consts import BloggerHostMap


class HostResolvingMiddleware(object):
    """automatic set query param ``blogger`` value according to request Host.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        host = request.META['HTTP_HOST']
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
