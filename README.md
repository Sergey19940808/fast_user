# fast_user

- Запуск спомощью docker-compose:
    1. git clone {url_repository}
    2. cd dir_fast_user
    3. Выполнить команду для заполнения env-файла:
        .env.dev файл - содержит переменные для dev-сборки
        .env.prod файл - содержит переменные для prod-сборки
        1) Первый случай, выполнить комманду:  cat .env.dev > .env
        2) Второй случай, выполнить комманду:  cat .env.prod > .env
        Будет создан файл .env который заполнится нужными переменными
    4. docker-compose up -d --build fast_user_api
    5. Открываем в браузере localhost:8000/
    
    
Задачи:
    Добавить команду для заполнения коллекции
