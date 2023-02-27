from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.home.as_view(), name='home')
]

