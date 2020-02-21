from django.db import transaction
from django.http import HttpResponse


@transaction.atomic
def index(request):
    return HttpResponse()
