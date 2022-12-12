from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer, RatingSerializer
from .models import Comment, Rate

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RatingViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RatingSerializer