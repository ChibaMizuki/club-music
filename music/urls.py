from django.urls import path
from .views import SongListView, SongCreateView, SongDeleteView, SongDetailView, SongEditView

urlpatterns = [
    path('', SongListView.as_view(), name='home'),
    path('create/', SongCreateView.as_view(), name='create'),
    path('<int:pk>/', SongDetailView.as_view(), name='detail'),
    path('song/<int:pk>/edit/', SongEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', SongDeleteView.as_view(), name='delete'),
]
