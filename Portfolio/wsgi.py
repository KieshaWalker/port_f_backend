"""
WSGI config for Portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

"""
WSGI config for Portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
import traceback

# Add the project directory to the Python path for Vercel
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("WSGI: Starting Django application", file=sys.stderr)
print(f"WSGI: Python path: {sys.path}", file=sys.stderr)
print(f"WSGI: Current directory: {os.getcwd()}", file=sys.stderr)

try:
    print("WSGI: Importing Django", file=sys.stderr)
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')
    print(f"WSGI: DJANGO_SETTINGS_MODULE set to: {os.environ.get('DJANGO_SETTINGS_MODULE')}", file=sys.stderr)

    print("WSGI: Getting WSGI application", file=sys.stderr)
    application = get_wsgi_application()
    print("WSGI: Django WSGI application loaded successfully", file=sys.stderr)

except Exception as e:
    print(f"WSGI: CRITICAL ERROR - Django WSGI application failed to load: {e}", file=sys.stderr)
    print("WSGI: Full traceback:", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    raise
