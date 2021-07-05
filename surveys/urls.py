from django.urls import path
from .views import *




urlpatterns = [
                path('auth/', auth_view, name='auth'),
                # Для Админов
                # Опрос
                path('survey_create/', survey_create, name='survey_create'),
                path('survey_update_del/<int:survey_id>', survey_update_del, name='survey_update_del'),
                path('survey_list/', survey_list, name='survey_list'),
                # Вопрос
                path('question_create/', question_create, name='question_create'),
                path('question_update_del/<int:question_id>', question_update_del, name='question_update_del'),
                # Для пользователей
                path('survey_active_list/', survey_active_list, name='survey_active_list'),
                path('answer_create/', answer_create, name='answer_create'),
                path('answer_view/<int:user_id>', answer_view, name='answer_view')
               ]
