Стандартный стек `FLASK + POSTGRESQL` с подключением к БД `PostgreSQL` и вьюхой страницы от которого можно ответвляться и писать свои приложения.
в файле `config.py` лежит конфигурация подключения к БД, где:
* `postgres` - это пользователь БД, а пароль не указан (ставится после двоеточия)
* `flask_app_db` - это БД, которую необходимо создать, чтобы к ней подключиться

___
<h4>Подробная информация о подключении</h4>:
`app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<ПОЛЬЗОВАТЕЛЬ>:<ПАРОЛЬ>@<IP-АДРЕС ХОСТА С БД>:<ПОРТ ХОСТА С БД>/<ИМЯ БД>'`

<h4>Образец подключения</h4>
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_postgres:user_password@127.0.0.1:5432/name_db'
---