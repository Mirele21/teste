from django.http import HttpResponse


def index(request):
    return HttpResponse("Isso é apenas um teste.")
