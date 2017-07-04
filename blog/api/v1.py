from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from blog.models import Post
from blog.serializers import SearchSerializer, BlogSearchSummarySerializer


def check_health(request):
    return HttpResponse('semo api/v1 ok')


class Search(APIView):
    def get(self, request):
        q = request.GET.get('q') or ''
        if not q:
            return JsonResponse({})
        posts = Post.objects.search(q)
        posts = posts[:10]  # FIXME: add page stragety later
        serializers = BlogSearchSummarySerializer(posts, many=True)
        serializer = SearchSerializer(data={'posts': serializers.data})
        return JsonResponse(serializer.initial_data)
