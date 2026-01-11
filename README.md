# Todo App (minimal Django)

Quick scaffolded Django project with a `todos` app and an "add todo" feature.

Setup (Windows):

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ to see the todo list and http://127.0.0.1:8000/add/ to add a todo.
