from django.conf.urls import url

from country.views import CountryListView, CountryRetrieveView, \
    CountryLeaderShipListView, CountryLeaderShipRetrieveView, \
    CountryNewsListView, CountryNewsRetrieveView, \
    CountryWinnerListView, CountryWinnerRetrieveView


urlpatterns = [
    url(r'^country/$', CountryListView.as_view(), name='countries'),
    url(r'^country/(?P<pk>[0-9]+)/$', CountryRetrieveView.as_view(), name='country'),

    url(r'^leadership/$', CountryLeaderShipListView.as_view(), name='country_leaderships'),
    url(r'^leadership/(?P<pk>[0-9]+)/$', CountryLeaderShipRetrieveView.as_view(), name='country_leadership'),

    url(r'^news/$', CountryNewsListView.as_view(), name='county_news_list'),
    url(r'^news/(?P<pk>[0-9]+)/$', CountryNewsRetrieveView.as_view(), name='country_news'),

    url(r'^winners/$', CountryWinnerListView.as_view(), name='county_news_list'),
    url(r'^winners/(?P<pk>[0-9]+)/$', CountryWinnerRetrieveView.as_view(), name='country_news'),

]