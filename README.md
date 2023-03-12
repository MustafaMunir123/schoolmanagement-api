
# schoolmanagement-api

### Getting started and running locally:


Make directory
```bash
  mkdir schoolmanagement_api
```
```bash
  cd schoolmanagement_api
```

Initialized empty git repository
```bash
  git init
```

Set remote origin
```bash
  git remote add origin https://github.com/MustafaMunir123/schoolmanagement-api.git
```

Take latest pull of master branch
```bash
  git pull origin master
```

Install packages
```bash
  pip install -r requirements.txt
```
Make database migrations
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

Run django-backend
```bash
  python manage.py runserver
```
