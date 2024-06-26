from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'url','url2', 'details']


class SongSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    sort_by = forms.ChoiceField(choices=[
        ('title', 'Title'),
        ('artist', 'Artist'),
    ], required=False, label='Sort By')
