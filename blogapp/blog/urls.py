from django.urls import path, include
from .views import HomeView,PostDetailView,AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('new_post/', AddPostView.as_view(), name='add_post'),
]