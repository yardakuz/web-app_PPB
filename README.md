1. Кузнецов Ярослав
2. https://drive.google.com/file/d/1nTTSmdbbJPnTCC3_Pi0oeIc5oFXFW0K2/view
3. В проектке реализован сервис, который принимает и отвечает на HTTP запросы. В нем содержатся три модели: города, улицы и магазины.

Реализованы запросы:
```
GET /city/ — получение всех городов из базы;
GET/city/ciyty_id/street/ — получение всех улиц города; (city_id — идентификатор города) 
РОЅТ/shop/ - создание магазина; Данный метод получает json с объектом магазина, в ответ возвращает id созданной записи. 
GET/shop/?street=&city=&open=0/1 - получение списка магазинов
```

Так же для удобства была добавлена главная страница, на которой можно выполнить GET city и shop запросы.

Сами модели: 
```
Магазин: 
• Название 
• Город 
• Улица 
• Дом 
• Время открытия 
• Время закрытия 

Город: 
• Название 

Улица: 
• Название 
• Город 
```

4. Для успешной работы проекта необходимо скачать postgreSQL 16.3 и установить пароль 1223

В командной строке (находясь в директории проекта) необходимо прописать``` pip install -r requirements.txt ```для установки корректных связей и скачивания библиотек нужных версий

Так как БД находится на локальной машине следует заполнить таблицы какими-то данными для проверки корректности работы задания

5. Логин и пароль от админки Jango соответсвенно - admin, 1223

6. Для запуска проекта в терминале (находясь в дериктории проекта) необходимо прописать команды:
```
cd PPB

python manage.py migrate

python manage.py runserver
```
