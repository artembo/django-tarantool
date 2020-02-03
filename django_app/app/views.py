import datetime

from django.db import transaction
from django.http import HttpResponse


@transaction.atomic
def index(request):
    import random
    import string

    # Create your tests here.
    from .models import MyModel

    def generate_name():
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(10))

    time_start = datetime.datetime.now()
    instances = []
    for _ in range(10000):
        instances.append(MyModel(name=generate_name()))
    MyModel.objects.bulk_create(instances)

    time_end = datetime.datetime.now()

    return HttpResponse(str(time_end - time_start))
