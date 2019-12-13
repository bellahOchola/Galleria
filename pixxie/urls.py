from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

urlpatterns=[
    url('^$', views.index, name= 'mainPage'),
    url(r'^img/(\d+)', views.single_photo, name = 'photo' )
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)