from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^ingest-login/$', views.ingest_login, name='ingest_login'),
    url(r'^ingest-reg/$', views.ingest_register, name='ingest_register'),
]
