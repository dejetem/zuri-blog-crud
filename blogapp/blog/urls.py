from django.urls import path, include
from .views import HomeView,PostDetailView,AddPostView,UpdatePostView,PostDeleteView,AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('new_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]