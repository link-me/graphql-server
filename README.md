# GraphQL Server

Python FastAPI + Strawberry GraphQL (вместо Node, т.к. Node недоступен в среде).

Возможности
- Типы `User`, `Post`; запросы `users`, `user(id)`, `posts`, `postsByAuthor(author_id)`.
- Мутации `createUser(name)`, `createPost(title, author_id)`.
- In-memory хранилище для простоты демо.

Быстрый старт
1. Создать окружение и установить зависимости:
   - `python -m venv .venv && .venv\Scripts\activate`
   - `pip install -r requirements.txt`
2. Запуск сервера: `uvicorn src.app:app --reload --port 8002`
3. Открыть GraphQL IDE: `http://127.0.0.1:8002/graphql`

Примеры запросов
- Создать пользователя:
```
mutation { createUser(name: "Alice") { id name } }
```
- Создать пост:
```
mutation { createPost(title: "Hello", author_id: 1) { id title author_id } }
```
- Получить пользователей:
```
{ users { id name } }
```
- Посты по автору:
```
{ postsByAuthor(author_id: 1) { id title } }
```

Заметки
- В продакшне заменить InMemory на БД; добавить авторизацию и расписать схемы.
- Strawberry даёт удобный IDE на `/graphql` для тестирования.
