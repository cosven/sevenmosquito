import mimetypes
import uuid

from django.conf import settings
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView

from .client import qiniu_client
from .consts import QINIU_BUCKET_NAME, QINIU_IMG_PREFIX
from .serializers import UploadCreateSerializer, UploadSerializer


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
        upload_create = UploadCreateSerializer(data=request.data)
        upload_create.is_valid(raise_exception=True)
        validated_data = upload_create.validated_data

        bucket_name = settings.QINIU_BUCKET_NAME
        ext = mimetypes.guess_extension(validated_data['content_type'])
        key = QINIU_IMG_PREFIX + uuid.uuid1().hex + ext
        token = qiniu_client.gen_token(bucket_name, key)
        upload = UploadSerializer(data=dict(
            token=token,
            key=key,
            bucket_name=QINIU_BUCKET_NAME,
            domain=settings.QINIU_SEMO_DOMAIN,
        ))
        return JsonResponse(upload.initial_data)
