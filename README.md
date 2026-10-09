# TUYIZERE Olivier Portfolio

A professional Django portfolio website for TUYIZERE Olivier, a software developer based in Kigali, Rwanda. The site highlights technical skills, projects, experience, education, training work, services, and a working contact form connected to SQLite.

## Features

- Responsive single-page portfolio layout
- Django-based backend and SQLite database
- Dynamic data-driven projects, skills, experience, education, and services
- Django admin management for all content types
- Contact form with validation, persistence, and success/error feedback
- Vanilla JavaScript for responsive navigation and scroll effects
- Clean CSS styling built from scratch without frontend frameworks

## Technologies

- Python
- Django
- HTML5
- CSS3
- Vanilla JavaScript
- SQLite

Project images can use remote URLs or local static assets stored in the project.

## Project Structure

```text
portfolio/
│
├── manage.py
├── portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── main/
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py
│   ├── migrations/
│   ├── models.py
│   ├── static/
│   │   └── main/
│   │       ├── css/
│   │       └── js/
│   ├── templates/
│   │   └── main/
│   ├── urls.py
│   └── views.py
├── media/
├── static/
├── requirements.txt
├── db.sqlite3
├── README.md
└── .gitignore
```

## Installation on Windows (PowerShell)

1. Create the project folder:

```powershell
mkdir "C:\portfolio-project"
cd "C:\portfolio-project"
```

2. Create a virtual environment:

```powershell
python -m venv .venv
```

3. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

4. Install Django:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

5. Create the Django project:

```powershell
django-admin startproject portfolio .
```

6. Create the app:

```powershell
python manage.py startapp main
```

7. Add your models and settings, then create migrations:

```powershell
python manage.py makemigrations main
python manage.py migrate
```

8. Create a superuser:

```powershell
python manage.py createsuperuser
```

9. Seed sample content:

```powershell
python manage.py seed_data
```

10. Run the development server:

```powershell
python manage.py runserver
```

11. Open Django Admin:

- Go to http://127.0.0.1:8000/admin/
- Log in with your superuser credentials

12. Add projects and content through Admin.

13. Add project images using a valid URL in the project admin form, or replace the sample URLs with local image paths if needed.

14. Test the contact form by visiting the main page and submitting a message.

## Configuration

If needed, you can override environment variables for production-like settings:

```powershell
$env:DJANGO_DEBUG = "False"
$env:DJANGO_ALLOWED_HOSTS = "localhost,127.0.0.1"
$env:DJANGO_SECRET_KEY = "your-secret-key"
$env:GITHUB_URL = "https://github.com/yourusername"
$env:LINKEDIN_URL = "https://www.linkedin.com/in/yourprofile"
$env:CONTACT_EMAIL = "your_email@example.com"
```

## Database Setup

This project uses SQLite by default for local development:

- Database file: `db.sqlite3`
- Migrations are stored in `main/migrations`

## Running the Project

```powershell
cd "C:\portfolio-project"
.\.venv\Scripts\Activate.ps1
python manage.py runserver
```

## Django Admin

The admin interface includes the following sections:

- Projects
- Skills
- Experience
- Education
- Services
- Contact messages

This makes the site easy to maintain without editing code.

## Deployment Information

Before deploying the project, prepare it for production:

- Set `DEBUG = False`
- Set `ALLOWED_HOSTS` to your actual domain names
- Store `SECRET_KEY` in environment variables
- Collect static files:

```powershell
python manage.py collectstatic
```

- Configure a production-grade database such as PostgreSQL or MySQL instead of SQLite for large or public deployments
- Use a production web server such as Gunicorn or uWSGI behind Nginx or Apache
- Keep `media/` and `staticfiles/` properly served by the hosting platform

## Notes

- The contact form saves messages into the SQLite database and is visible in Django Admin.
- Social media URLs are easy to update from settings through environment variables.
- The project is structured so it can be extended with more portfolio entries later.
