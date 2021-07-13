import logging

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from django.shortcuts import get_object_or_404
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView

from .serializers import *
from django.utils import timezone



# Для Админов
@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def survey_create(request):
    """Метод добавляет опрос
    Пример POST запроса в теле JSON:
    {
        "name": "опрос 3",
        "start_date": "2021-07-03T17:10:00+03:00",
        "end_date": "2021-07-10T17:14:00+03:00",
        "survey_description": "Опрос 3"
}
    """
    serializer = Surveyserializers(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def survey_update_del(request, survey_id):
    """Метод для обновления удаления опроса
        Для обновления пример
        PATCH запроса в теле JSON
        {
            "name": "опрос 3",
            "end_date": "2021-07-10T17:14:00+03:00",
            "survey_description": "Опрос 3"
        }
        Поле start_date неизменяемое
    """
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.method == 'PATCH':
        serializer = Surveyserializers(survey, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        survey.delete()
        return Response('{"Detail": "Survey DELETE"', status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def survey_list(request):
    """
    Возвращает список  активных и не активных Опросов

    """
    surveys = Survey.objects.all()
    serializer = Surveyserializers(surveys, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_create(request):
    """Метод добавляет вопрос в Опрос
    Пример POST запроса в теле JSON:
     {
            "survey": 1,
            "question": "Вопрос 1",
            "question_type": ""CHOICE"
    }
    В поле "survey": 1, передаётся id существующего опроса
    """
    serializer = QuestionSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_update_del(request, question_id):
    """Метод для обновления удаления вопроса
        Для обновления пример
        PATCH запроса в теле JSON
        {
                "survey": 1,
                "question": "Вопрос 1",
                "question_type": "CHOICE"

        }
       При изменении поля  "survey" можно перенести вопрос в другой опрос.
        По умолчанию поле "question_type": "TEXT"
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        question.delete()
        return Response('{"Detail": "Question DELETE"', status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def variants_create(request):
    """Метод добавляет вопрос в Опрос
    Пример POST запроса в теле JSON:
     {

            "question": 1,
            "answer_option": "ДА"
    }
    В поле "question": 1, передаётся id существующего вопроса

    """
    serializer = VariantsSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def variants_update_del(request, variants_id):
    """Метод для обновления удаления ответа
        Для обновления пример
        PATCH запроса в теле JSON
        {
                "question": 1,
                "answer_option": "ДА"
        }
       При изменении поля  "survey" можно перенести вопрос в другой опрос.
    """
    variants = get_object_or_404(Variants, pk=variants_id)
    if request.method == 'PATCH':
        serializer = VariantsSerializer(variants, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        variants.delete()
        return Response('{"Detail": "Variants DELETE"', status=status.HTTP_204_NO_CONTENT)


#Для Пользователей
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def survey_active_list(request):
    """Метод возвращает список активных опросов"""
    survey = Survey.objects.filter(end_date__gte=timezone.now()).filter(start_date__lte=timezone.now())
    serializer = Surveyserializers(survey, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def answer_create(request):
    """Метод добавляет вопрос в Опрос
            Пример POST запроса в теле JSON:
             {
                "user_id": 1,
                "survey": 1,
                "quest": 5,
                "variant": 4,
                "variant_text": null
            }
            """
    serializer = AnswerSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def answer_view(request, user_id):
    """
    Метод возращает список ответов пользователя.
    """
    answer = Answer.objects.filter(user_id=user_id)
    serializer = AnswerSerializer(answer, many=True)
    return Response(serializer.data)