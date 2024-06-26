from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Song
from .forms import SongForm

class SongListView(ListView):
    model = Song
    template_name = 'home.html'
    context_object_name = 'songs'
    ordering = ['pk']  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        songs = context['songs']
        for index, song in enumerate(songs, start=1):
            song.display_number = index
        return context


class SongCreateView(CreateView):
    model = Song
    form_class = SongForm
    template_name = 'song_form.html'
    success_url = reverse_lazy('home')


class SongDeleteView(DeleteView):
    model = Song
    template_name = 'song_delete.html'
    success_url = reverse_lazy('home')


class SongDetailView(DetailView):
    model = Song
    template_name = 'song_detail.html'
    context_object_name = 'song'


class SongEditView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'song_form.html'
    success_url = reverse_lazy('home')
