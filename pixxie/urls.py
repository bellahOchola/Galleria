from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns=[
    url('^$', views.index, name= 'mainPage'),
    url(r'^img/(\d+)', views.single_photo, name = 'photo' ),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)', views.location_pixxies, name='location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)