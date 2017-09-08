from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    album_logo = models.FileField()
    def get_absolute_url(self):
        return reverse('music:details',kwargs={'pk':self.pk})
    def __str__(self):
        return self.album_title + '-' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    myfile = models.FileField(default='C:\\New folder\\mp3\\Shot.mp3')
    def get_absolute_url(self):
        return reverse('music:details',kwargs={'pk':self.pk})
    def __str__(self):
        return self.song_title