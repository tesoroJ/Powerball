from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /DB_connect/
    url(r'^$', views.index, name='index'),
    ]