# Blog App

A simple Django-based blog application that allows users to create posts, categorize them, and comment on posts.

## Features

- List all blog posts
- View detailed post pages with comments and categories
- Admin interface for managing posts, comments, and categories
- Responsive Bootstrap-based UI

## Project Structure

```
blog/
├── blog/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── post/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── post/
│   │       ├── base.html
│   │       ├── post_detail.html
│   │       └── post_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
```

## Getting Started

### Prerequisites

- Python 3.8+
- Django 5.x

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/jennihunt/Django_BlogApp.git
    cd blog
    ```

2. Install dependencies:

    ```sh
    pip install django
    ```

3. Apply migrations:

    ```sh
    python manage.py migrate
    ```

4. Create a superuser for the admin interface:

    ```sh
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```sh
    python manage.py runserver
    ```

6. Access the app at [http://localhost:8000/](http://localhost:8000/)

## Usage

- Visit the home page to see the list of posts.
- Click on a post to view details, comments, and categories.
- Log in to the admin interface at `/admin/` to manage posts, comments, and categories.

## Project Structure

- `blog/` - Django project configuration
- `post/` - Main app for posts, comments, and categories

## License

This project is for educational purposes.
