from rest_framework.serializers import ModelSerializer
from .models import Comment, Rate


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'