# djit_theme - Django Theme App

This app is set up as a theme that can be added into the Django project and it will support:

- Tailwind CSS
- Alpine.js
- DaisyUI
- htmx
- Some of the associated tooling.

I'm building this for my own applications, and thought I would share.

It might be useful one day!


## For Tailwind

```python
## Add Tailwind Support
INTERNAL_IPS.append("127.0.0.1")

INSTALLED_APPS.extend([
    'tailwind',
    'djit_theme',
    'django_browser_reload'
])

TAILWIND_APP_NAME = 'djit_theme'

MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")
## End Tailwind Support
```

```sh
python manage.py tailwind install
```

```sh
python manage.py tailwind start
```

## For htmx

```python
## Add HTMX Support
STATICFILES_DIRS.append(BASE_DIR / "static")
INSTALLED_APPS.append("django_htmx")
MIDDLEWARE.append("django_htmx.middleware.HtmxMiddleware")
## End HTMX Support
```

```sh
mkdir static
mkdir static/assets
mkdir static/assets/js
```

```sh
curl -o static/js/htmx.min.js https://unpkg.com/htmx.org@1.9.12/dist/htmx.min.js
```

```html
{% load static %}
<script src="{% static 'htmx.min.js' %}" defer></script>
```

## For Alpine

```sh
curl -o static/js/alpine.min.js https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js
```

```html
{% load static %}
<script src="{% static 'alpine.min.js' %}" defer></script>
```