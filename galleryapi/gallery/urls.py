from django.urls import path
from .views import GalleryImageListCreateView, GalleryImageRetrieveDestroyView

urlpatterns = [
    path('images/', GalleryImageListCreateView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', GalleryImageRetrieveDestroyView.as_view(), name='image-retrieve-destroy'),
]