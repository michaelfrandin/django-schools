from ..models import Quiz
from rest_framework import serializers, viewsets


class QuizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['name', 'subject']

class QuizesViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizesSerializer