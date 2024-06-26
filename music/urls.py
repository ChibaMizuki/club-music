from django.urls import path
from .views import SongListView, SongCreateView, SongDeleteView, SongDetailView

urlpatterns = [
    path('', SongListView.as_view(), name='home'),
    path('registration/', SongCreateView.as_view(), name='registration'),
    path('delete/<int:pk>/', SongDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', SongDetailView.as_view(), name='detail'),
]
