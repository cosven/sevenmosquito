from django.conf import settings
from qiniu import Auth


class QiniuClient(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    @property
    def client(self):
        return Auth(self.key, self.secret)

    def gen_token(self, bucket_name, key, expire=3600):
        return self.client.upload_token(bucket_name, key, expire)


qiniu_client = QiniuClient(settings.QINIU_ACCESS_KEY,
                           settings.QINIU_ACCESS_SECRET)
