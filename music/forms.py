from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'number', 'artist', 'url','url2', 'details']
        labels = {
            'title': 'タイトル',
            'number': '登録番号',
            'artist': 'アーティスト',
            'url': 'URL',
            'url2': '他URL',
            'details': '補足',
        }
        error_messages = {
            'title': {
                'required': 'タイトルを入力'
            },
            'number': {
              'unique': 'この番号は既に登録済みです'  
            },
            'artist': {
                'required': 'アーティスト名を入力'
            },
            'url': {
                'required': 'URLを入力'
            }
        }


class SongSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    sort_by = forms.ChoiceField(choices=[
        ('title', 'Title'),
        ('artist', 'Artist'),
    ], required=False, label='Sort By')
