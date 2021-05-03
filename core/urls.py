from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="docs")),
    path("api/", include("courses.urls")),
    path(
        "openapi/",
        get_schema_view(
            title="Ypy school",
            description="API for all things …",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="swagger-ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="docs",
    ),
]
