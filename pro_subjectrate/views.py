from django.http import HttpResponse

from . import settings


def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)