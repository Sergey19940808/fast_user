# fast_user

- Запуск спомощью docker-compose:
    1. git clone {url_repository}
    2. cd dir_fast_user
    3. Выполнить команду для заполнения env-файла:
        1) .env.dev - содержит переменные для dev-сборки
        2) .env.prod - содержит переменные для prod-сборки
        3) Первый случай:  > .env | cat .env.dev > .env
        4) Второй случай:  > .env | cat .env.prod > .env
        5) Будет создан файл .env который заполнится нужными переменными
    4. docker-compose up -d --build fast_api_user
    5. sh ./libs/scripts/scripts_set_app/setup_fast_user_app.sh
    6. Открываем в браузере localhost:8000/
