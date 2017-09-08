from django.views import generic
from .models import Album,Song
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()
class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
class SongCreate(CreateView):
    model = Song
    fields = ['album','file_type','song_title','myfile']