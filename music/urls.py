from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'music'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailsView.as_view(),name='details'),
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-edit'),
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$',views.SongCreate.as_view(),name='song-add'),
]
