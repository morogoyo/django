from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$', views.index , name = 'jobs'),
    url(r'^search', views.search , name = 'search'),
    url(r'^result', views.search , name = 'search_result'),

]
