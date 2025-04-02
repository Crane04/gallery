from rest_framework import generics
from .models import GalleryImage
from .serializers import GalleryImageSerializer

class GalleryImageListCreateView(generics.ListCreateAPIView):
    queryset = GalleryImage.objects.all().order_by('-uploaded_at')
    serializer_class = GalleryImageSerializer

class GalleryImageRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer