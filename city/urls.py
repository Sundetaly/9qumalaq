from django.conf.urls import url

from city.views import CityListView, CityRetrieveView, \
    NewsRetrieveView, NewsListView, \
    LeaderShipRetrieveView, LeaderShipListView, \
    WinnerRetrieveView, WinnerListView, \
    LeaderShipCityView, WinnerCityView, NewsCityView


urlpatterns = [
    url(r'^city/$', CityListView.as_view()),
    url(r'^city/(?P<pk>[0-9]+)/$', CityRetrieveView.as_view()),
    url(r'^city/(?P<pk>[0-9]+)/leaderships$', LeaderShipCityView.as_view()),
    url(r'^city/(?P<pk>[0-9]+)/winners$', WinnerCityView.as_view()),
    url(r'^city/(?P<pk>[0-9]+)/news$', NewsCityView.as_view()),

    url(r'^leadership/$', LeaderShipListView.as_view()),
    url(r'^leadership/(?P<pk>[0-9]+)/$', LeaderShipRetrieveView.as_view()),

    url(r'^news/$', NewsListView.as_view()),
    url(r'^news/(?P<pk>[0-9]+)/$', NewsRetrieveView.as_view()),

    url(r'^winners/$', WinnerListView.as_view()),
    url(r'^winners/(?P<pk>[0-9]+)/$', WinnerRetrieveView.as_view()),
]