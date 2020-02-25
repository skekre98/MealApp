from django.conf.urls import url

from . import views
from . import login

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^ingest-login/$', login.user_login, name='ingest_login'),
    url(r'^ingest-reg/$', register.ingest_register, name='ingest_register'),
]
