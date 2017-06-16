import mimetypes
import uuid


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView

from .client import qiniu_client
from .consts import QINIU_BUCKET_NAME
from .serializers import UploadCreateSerializer, UploadSerializer

# Create your views here.


def check_health(request):
    return HttpResponse('semo/upload ok.')


class Upload(APIView):

    def get(self, request):
        return HttpResponse('OK')

    @method_decorator(login_required)
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
        upload_create = UploadCreateSerializer(data=request.data)
        upload_create.is_valid(raise_exception=True)
        validated_data = upload_create.validated_data

        bucket_name = settings.QINIU_BUCKET_NAME
        ext = mimetypes.guess_extension(validated_data['content_type'])
        key = uuid.uuid1().hex + ext
        token = qiniu_client.gen_token(bucket_name, key)
        upload = UploadSerializer(data=dict(
            token=token,
            key=key,
            bucket_name=QINIU_BUCKET_NAME
        ))
        return JsonResponse(upload.initial_data)
