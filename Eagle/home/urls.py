from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
]
