# User_Survey
#Управление
Запуск

1) Выполняем команду:
    docker build .
2) Собираем образ командой:
  docker-compose build
3)Как только образ будет собран, запускаем контейнер:
  docker-compose up -d
4) Переходим по адресу
  http://127.0.0.1:8000/api/
 Пользователь админ уже добавлен.
    User: admin
    Pass: admin
API 
1)Добавление опроса. 
    http://127.0.0.1:8000/api/survey_create/
    Метод добавляет опрос
    Пример POST запроса в теле JSON:
    {
    "name": "опрос 3",
    "start_date": "2021-07-03T17:10:00+03:00",
    "end_date": "2021-07-10T17:14:00+03:00",
    "survey_description": "Опрос 3"
    }
2) Обновить/удалить опрос.
    http://127.0.0.1:8000/survey_update_del/<int:survey_id>
    <int:survey_id> - id опроса
    Метод для обновления удаления опроса
    Для обновления пример
    PATCH запроса в теле JSON
    {
    "name": "опрос 3",
    "end_date": "2021-07-10T17:14:00+03:00",
    "survey_description": "Опрос 3"
    }
    Поле start_date неизменяемое.

3)  Возвращает список активных и не активных Опросов.
    http://127.0.0.1:8000/api/survey_list/
   

4) Для добавления опроса в опрос.
    http://127.0.0.1:8000/api/question_create/
    Метод добавляет вопрос в Опрос
    Пример POST запроса в теле JSON:
    {
    "survey": 1,
    "question": "Вопрос 1",
    "question_type": ""CHOICE"
    }
    В поле "survey": 1, передаётся id существующего опроса.
5)Обновить/удалить вопрос.
    http://127.0.0.1:8000/api/question_update_del/<int:question_id>
    <int:question_id> id вопроса.
    Метод для обновления удаления вопроса
    Для обновления пример
    PATCH запроса в теле JSON
    {
    "survey": 1,
    "question": "Вопрос 1",
    "question_type": "CHOICE"

    }
    При изменении поля "survey" можно перенести вопрос в другой опрос.
    По умолчанию поле "question_type": "TEXT"
6) Список активных вопросов.
    http://127.0.0.1:8000/api/survey_active_list/
7) Добавить ответ.
    Метод добавляет вопрос в Опрос
    Пример POST запроса в теле JSON:
    {
    "user_id": 1,
    "survey": 1,
    "quest": 5,
    "variant": 4,
    "variant_text": null
    }
8) Список ответов пользователя.
    http://127.0.0.1:8000/api/answer_view/<int:user_id>
    где <int:user_id> - ID пользователя.