from django.conf.urls import url

from country.views import CountryListView, CountryRetrieveView, \
    LeaderShipListView, LeaderShipRetrieveView, \
    NewsListView, NewsRetrieveView, \
    WinnerListView, WinnerRetrieveView, \
    LeaderShipCountryView, NewsCountryView, WinnerCountryView


urlpatterns = [
    url(r'^country/$', CountryListView.as_view(), name='countries'),
    url(r'^country/(?P<pk>[0-9]+)/$', CountryRetrieveView.as_view(), name='country'),
    url(r'^country/(?P<pk>[0-9]+)/leaderships$', LeaderShipCountryView.as_view()),
    url(r'^country/(?P<pk>[0-9]+)/winners$', WinnerCountryView.as_view()),
    url(r'^country/(?P<pk>[0-9]+)/news$', NewsCountryView.as_view()),

    url(r'^leadership/$', LeaderShipListView.as_view(), name='country_leaderships'),
    url(r'^leadership/(?P<pk>[0-9]+)/$', LeaderShipRetrieveView.as_view(), name='country_leadership'),

    url(r'^news/$', NewsListView.as_view(), name='county_news_list'),
    url(r'^news/(?P<pk>[0-9]+)/$', NewsRetrieveView.as_view(), name='country_news'),

    url(r'^winners/$', WinnerListView.as_view(), name='county_news_list'),
    url(r'^winners/(?P<pk>[0-9]+)/$', WinnerRetrieveView.as_view(), name='country_news'),

]