from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
