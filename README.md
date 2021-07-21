

# User_Survey
## Задача ##
Cпроектировать и разработать API для системы опросов пользователей.

Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя
## Управление ##
### Запуск ###

1) Выполняем команду: 
```
  docker-compose up -d
 ```
    
2) Переходим по адресу
```
  http://127.0.0.1:8000/api/
  ```
  Пользователь админ уже добавлен.
 >User: admin
 >
 >Pass: admin
### Авторизация пользователя ###
1) Отправьте POST запрос, по адресу:
```
  http://127.0.0.1:8000/api/token/
```
В теле JSON:
```
    {
      "username": "",
      "password": ""
  }
```
На выходе получите token access  и refresh. 

2) Для обновления TOKEN
 Отправьте POST запрос:
```
  http://127.0.0.1:8000/api/token/refresh/
```
 В теле JSON:
```
  {
    "refresh": ""
  }
```
3) Для авторизации:
 в Hefders добавит ключ Authorization с значением Bearer <token  access>
### API ###

1)Добавление опроса.

 ```   
   http://127.0.0.1:8000/api/survey_create/
```    
  * Метод добавляет опрос
   Пример POST запроса в теле JSON.  
   ```
   {
      "name": "опрос 3",
      "start_date": "2021-07-03T17:10:00+03:00",
      "end_date": "2021-07-10T17:14:00+03:00",
      "survey_description": "Опрос 3"
    }
 ```
2) Обновить/удалить опрос.
 ```
   http://127.0.0.1:8000/survey_update_del/[int:survey_id]
 ```
   * [int:survey_id] - id опроса
    
  Метод для обновления удаления опроса
  Для обновления пример PATCH запроса в теле JSON
  ```
    {
      "name": "опрос 3",
      "end_date": "2021-07-10T17:14:00+03:00",
      "survey_description": "Опрос 3"
      }
   ```

  #### Поле start_date неизменяемое. ####

3)  Возвращает список активных  Опросов.
```
  http://127.0.0.1:8000/api/survey_list/
```   

4) Для добавления опроса в опрос.
```
   http://127.0.0.1:8000/api/question_create/
```  
   Метод добавляет вопрос в Опрос
   Пример POST запроса в теле JSON:
   ```
    {
    "survey": 1,
    "question": "Вопрос 1",
    "question_type": ""CHOICE"
    }
   ```
   #### В поле "survey": 1, передаётся id существующего опроса. ####
5)Обновить/удалить вопрос.
 ```
    http://127.0.0.1:8000/api/question_update_del/[int:question_id]
 ```
   * [int:question_id] id вопроса.
    
   Метод для обновления удаления вопроса.
   Для обновления пример.
   PATCH запроса в теле JSON.
  ```
    {
    "survey": 1,
    "question": "Вопрос 1",
    "question_type": "CHOICE",
    "variants": []
    }
  ```
  #### При изменении поля "survey" можно перенести вопрос в другой опрос.
  #### По умолчанию поле "question_type": "TEXT" ####
  #### "variants": [] - это список вариантов ответов, если такие, имеются.
 
6) Добавить ответ.
```
    http://127.0.0.1:8000/apianswer_create/
 ```
    Метод добавляет вопрос в Опрос.
    Пример POST запроса в теле JSON
   ```
    {
      "user_id": 1,
      "survey": 1,
      "quest": 5,
      "variant": 4,
      "variant_text": null
    }
   ```
7) Список ответов пользователя.
```
    http://127.0.0.1:8000/api/answer_view/[int:user_id]
```  
    * [int:user_id] - ID пользователя.
