![example workflow](https://github.com/BaikoIlya/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

IP: 178.154.192.231

### Описание:

Проект YaMDb собирает отзывы пользователей на различные произведения.

### Пользовательские роли
**Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

**Аутентифицированный пользователь (user)** — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.

**Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.

**Администратор (admin)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

**Суперюзер Django** — обладет правами администратора (admin)

Для аутентификации используйте JWT-токены.

###### Доступные адресса запросов:

1. .../api/v1/auth/signup/ (POST)
2. .../api/v1/auth/token/ (POST)
3. .../api/v1/categories/ (GET, POST, DEL)
4. .../api/v1/genres/ (GET, POST, DEL)
5. .../api/v1/titles (GET, POST)
6. .../api/v1/titles/{titles_id} (GET, PATCH, DEL)
7. .../api/v1/titles/{title_id}/reviews/ (GET, POST)
8. .../api/v1/titles/{title_id}/reviews/{review_id}/ (GET, PATCH, DEL)
9. .../api/v1/titles/{title_id}/reviews/{review_id}/comments/ (GET, POST)
10. .../api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ (GET, PATCH, DEL)
11. .../api/v1/users/ (GET, POST)
12. .../api/v1/users/{username}/ (GET, PATCH, DEL)
13. .../api/v1/users/me/ (GET, PATCH)

### Установка:

Для начала вам необходимо сделать Fork данного проекта к себе в профиль.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/<ваш_ник>/<Имя_проекта>.git
```

Перейти в настройки проекта и добавить Reppository Secrets

```
DB_ENGIINE= # Основа базы данных
DB_NAME= # Имя базы данных
POSTGRES_USER= # Супер прользователь для взаимодействия с базой
POSTGRES_PASSWORD= # Пароль для пользователя
DB_HOST= # Хост внутри контейнера для базы данных
DB_PORT= # Порт внутри контейра
DOCKER_USERNAME= #Имя пользователя для DOCKER HUB
DOCKER_PASSWORD= #Пароль от DOCKER HUB
HOST= # IP облачного сервиса
PASSPHRASE= # Пароль от приватного ключа
TELEGRAM_TO= # Id получателя сообщения в телеграм
TELEGRAM_TOKEN= #ID Telegram bota
```

Внесите изменения в файле /infra/docker-compose.yaml

```
web:
  image: <ник Docker_hub>/<имя_проекта>:latest
```

Выполнить пушь проекта на github.

После получения сообщения об успешном развертывании, подключиться на удаленный сервер и выполнить миграции:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```

Наполнить базу данными:

```
docker-compose exec web python manage.py loaddata fixtures.json

```

