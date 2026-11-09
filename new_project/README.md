# DataLab learning website

A Django starter site for a practical data science and AI learning platform. It includes a responsive landing page, course catalog and detail pages, and a contact/enrollment inquiry form saved to SQLite and manageable through Django admin.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Apply database migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`
5. Visit http://127.0.0.1:8000/

To manage inquiries, create an admin account with `python manage.py createsuperuser` and visit `/admin/`.

The development settings use a placeholder secret key and `DEBUG = True`; configure environment-based settings and production security options before deployment.
