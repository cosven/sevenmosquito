import mimetypes
import uuid

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from .client import qiniu_client

# Create your views here.


def check_health(request):
    return HttpResponse('semo/upload ok.')


class Upload(APIView):

    def get(self, request):
        return HttpResponse('OK')

    def post(self, request):
        """create a upload

        .. http:post:: /api/v1/upload/

            :jsonparam content_type: file content type


        response json example::

            {
                "token": "",
                "key": "",
                "bucket_name": ""
            }
        """
        return HttpResponse('OK')
        bucket_name = settings.QINIU_BUCKET_NAME
        ext = mimetypes.guess_extension()
        if ext is None:
            return JsonResponse({})
        key = uuid.uuid1() + '.' + ext
        token = qiniu_client.gen_token(bucket_name, key)
        return JsonResponse({})
