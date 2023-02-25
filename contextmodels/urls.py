# -*- coding: utf-8 -*-
from django.urls import path
from django.views.generic import TemplateView

from . import views  # noqa: F401


app_name = 'contextmodels'
urlpatterns = [
    path(r'', TemplateView.as_view(template_name="base.html")),
]
