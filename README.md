Проект бэкенда для склада рулонов металла.
Используемый стек: FastAPI, SQLAlchemy, pydantic.
Реализованы: 
1.POST /coil. Добавление нового рулона на склад. Длина и вес обязательно должны быть 
заданы. Возвращает назначенный id рулона.
2. DELETE /coil. Удаление рулона с указанным id со склада.
3. GET /coil. Получение списка рулонов со склада по указанному диапазону id / веса / длины /
даты добавления / даты удаления со склада.
4. GET /coil/stats. 
Получение статистики по рулонам за определённый период:
 количество добавленных рулонов;
 количество удалённых рулонов;
 средняя длина, вес рулонов, находившихся на складе в этот период;
 максимальная и минимальная длина и вес рулонов, находившихся на складе 
в этот период;
 суммарный вес рулонов на складе за период;
 максимальный и минимальный промежуток между добавлением и удалением 
рулона.

БД - SQLite.
Конфигурации к подключению к БД настраиваются через файл config

Обработаны стандартные кейсы ошибок.

Проект обёрнут в Docker.

Также дополнительно:
1. GET /coil берёт на вход комбинацию диапазонов.
2. GET /coil/stats дополнительно возвращает: 
2.1. День, когда на складе находилось минимальное и максимальное количество 
рулонов за указанный период.
2.2. День, когда суммарный вес рулонов на складе был минимальным и 
максимальным в указанный период.
3. Написаны некоторые тесты для проверки работоспособности сервера (не pytest).
