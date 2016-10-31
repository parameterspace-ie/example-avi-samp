from django.conf.urls import include, patterns, url
from avi import views


urlpatterns = patterns(
    '',
    url(r'^$',
        views.index,
        name='index'),
)
