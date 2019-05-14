from django.conf import settings


def common(request):
    return {'APP_NAME': settings.APP_NAME}
