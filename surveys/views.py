from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.utils import timezone


class Surve_ViewSet(ModelViewSet):
    model = Survey
    queryset = model.objects.all()
    serializer_class = Surveyserializers

    def list(self, request):
        survey = Survey.objects.filter(end_date__gte=timezone.now()).filter(start_date__lte=timezone.now())
        serializer = Surveyserializers(survey, many=True,)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission()  for permission in permission_classes]


class Questions_ViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class Answer_ViewSet(ModelViewSet):
    queryset = Answer.objects.none()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, user_id):
        answer = Answer.objects.filter(user_id=user_id)
        serializer = AnswerSerializer(answer, many=True,)
        return Response(serializer.data)