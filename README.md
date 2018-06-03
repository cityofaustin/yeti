# yeti

A cooler way for residents to suggest changes to austin.gov

## Getting started

### 1-time setup

1. Install python3
2. `python -m venv .env`
3. `. .env/bin/activate`
4. `pip install --requirement deploy/requirements.txt`

### Running the API

1. `. .env/bin/activate`
2. `python manage.py runserver`

## Testing the API

### via curl

```
curl \
    --header 'content-type: application/json' \
    --data '{"email":"fakeemail@gmail.com","url":"blah.com", "suggestions":[{"name_of_component":"textbox","original_text":"hahahahaah i am fake text please edit me", "altered_text":"hahahahaah I am edited text!!!","language":"Arabic","reason":"poor translation"}]}' \
    http://localhost:8000/wiki/
```

```
make migrations
python manage.py makemigrations
```

```
migrate
python manage.py migrate
```
