from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from rest_framework.views import APIView

from blog.models import Post
from blog.serializers import (
    SearchSerializer,
    BlogSearchSummarySerializer,
    BlogUpdateSerializer,
)


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


class Blog(APIView):
    @method_decorator(login_required)
    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = BlogUpdateSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'ok': True})
        return JsonResponse(dict(errors=serializer.errors), status=400)
