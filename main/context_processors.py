from django.conf import settings


def site_settings(request):
    return {
        "site_name": getattr(settings, "SITE_NAME", "TUYIZERE Olivier"),
        "social_links": getattr(settings, "SOCIAL_LINKS", {}),
    }
