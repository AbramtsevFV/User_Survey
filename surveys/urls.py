from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

surve_list = Surve_ViewSet.as_view(
    {
        'get': 'list',
        'post': 'create',
     }
)

surve_detail = Surve_ViewSet.as_view(
    {
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)

question = Questions_ViewSet.as_view(
    {
        'post': 'create',
    }
)

question_datail = Questions_ViewSet.as_view(
    {
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    }
)


urlpatterns = [
                # Получение доступа
                path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                # Для Админов
                # Опрос
                path('survey_create/', surve_list, name='surve_create'),
                path('survey_update_del/<int:pk>', surve_detail, name='survey_update_del'),
                # Вопрос
                path('question_create/', question, name='question_create'),
                path('question_update_del/<int:pk>', question_datail, name='question_update_del'),
                # Для пользователей
                path('survey_list/', surve_list, name='surve_list'),
                path('answer_create/', Answer_ViewSet.as_view({'post': 'create'}), name='answer_create'),
                path('answer_view/<int:user_id>', Answer_ViewSet.as_view({'get': 'retrieve'}), name='answer_view')
            ]
