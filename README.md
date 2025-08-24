# Django Blog

A simple web blog built with [Django 5](https://docs.djangoproject.com/en/5.2/). This project demonstrates core Django features such as models, views, templates, forms, admin customization, and user comments.

## Features

- List, view, and share blog posts
- Add comments to posts
- Admin interface for managing posts and comments
- Pagination for post lists
- Email sharing of posts (configurable via `.env`)
- Custom styling with CSS

## Project Structure

```
django_blog/
    blog/
        admin.py
        apps.py
        forms.py
        models.py
        tests.py
        urls.py
        views.py
        migrations/
        static/
        templates/
    django_blog/
        settings.py
        urls.py
        wsgi.py
        asgi.py
    manage.py
    db.sqlite3
    .env
    .gitignore
    pyproject.toml
    poetry.lock
    README.md
```

## Getting Started

### Requirements

- Python 3.12+
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/gabrielspires/Django5-WebBlog.git
    ```

2. **Install dependencies:**
    ```sh
    poetry install
    ```

3. **Create the `.env` file:**

    The `.env` file is required for email functionality and should be placed in the project root. **Do not commit this file to version control.**

    Example `.env`:
    ```
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_email_password
    DEFAULT_FROM_EMAIL=Your Name <your_email@example.com>
    ```

    - `EMAIL_HOST_USER`: The email address used to send emails.
    - `EMAIL_HOST_PASSWORD`: The password for the email account.
    - `DEFAULT_FROM_EMAIL`: The default "from" address for outgoing emails.

    For this project you don't need to fill in the password field since django is configured to use the console as the email backend, not a real SMTP server.

4. **Apply migrations:**
    ```sh
    poetry run python manage.py migrate
    ```

5. **Create a superuser (for admin access):**
    ```sh
    poetry run python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    poetry run python manage.py runserver
    ```

7. **Access the blog:**
    - Blog: [http://localhost:8000/blog/](http://localhost:8000/blog/)
    - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Development

- Static files are located in `blog/static/`
- Templates are in `blog/templates/`
- Admin customization is in `blog/admin.py`
- Models are in `blog/models.py`
- Views are in `blog/views.py`
- URL configuration is in `blog/urls.py` and `django_blog/urls.py`

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).  
See the [LICENSE](LICENSE) file for details.