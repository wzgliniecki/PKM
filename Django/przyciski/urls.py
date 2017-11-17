from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^trains$', views.przyciski_list),
    url(r'^trains/(?P<pk>[0-9]+)/$', views.przyciski_detail),
]