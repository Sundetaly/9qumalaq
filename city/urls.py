from django.conf.urls import url

from city.views import CityListView, CityRetrieveView, \
    CityNewsRetrieveView, CityNewsListView, \
    CityLeaderShipRetrieveView, CityLeaderShipListView


urlpatterns = [
    url(r'^city/$', CityListView.as_view()),
    url(r'^city/(?P<pk>[0-9]+)/$', CityRetrieveView.as_view()),

    url(r'^leadership/$', CityLeaderShipListView.as_view()),
    url(r'^leadership/(?P<pk>[0-9]+)/$', CityLeaderShipRetrieveView.as_view()),

    url(r'^news/$', CityNewsListView.as_view()),
    url(r'^news/(?P<pk>[0-9]+)/$', CityNewsRetrieveView.as_view()),
]