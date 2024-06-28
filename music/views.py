from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Song
from .forms import SongForm, SongSearchForm
from django.db.models import Q

class SongListView(ListView):
    model = Song
    template_name = 'home.html'
    context_object_name = 'songs'
    ordering = ['number']  
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = SongSearchForm(self.request.GET or None)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            sort_by = form.cleaned_data.get('sort_by')
            print(form.cleaned_data)
            if sort_by and query:
                if sort_by == 'title':
                    queryset = queryset.filter(title__icontains=query)
                elif sort_by == 'artist':
                    queryset = queryset.filter(artist__icontains=query)
        return queryset


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
