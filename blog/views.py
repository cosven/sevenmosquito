from django.http import HttpResponse


def check_health(request):
    return HttpResponse('semo ok.')


def index(request):
    print(request.META['HTTP_HOST'])
    return HttpResponse('homepage')

def yannnli_index(request):
    return HttpResponse("<h1>Yannnli, you're the best. oyi ~</h1>")
