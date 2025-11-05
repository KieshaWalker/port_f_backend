#!/usr/bin/env python
import os
import sys
import traceback

# Add the parent directory to the Python path so we can import Portfolio
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

print("INDEX: Starting Vercel function", file=sys.stderr)
print(f"INDEX: Python path: {sys.path}", file=sys.stderr)
print(f"INDEX: Current directory: {os.getcwd()}", file=sys.stderr)

# Check what packages are available
print("INDEX: Checking available packages", file=sys.stderr)
try:
    import django
    print(f"INDEX: Django available: {django.VERSION}", file=sys.stderr)
except ImportError as e:
    print(f"INDEX: Django not available: {e}", file=sys.stderr)

try:
    import ninja
    print(f"INDEX: Ninja available: {ninja.__version__}", file=sys.stderr)
except ImportError as e:
    print(f"INDEX: Ninja not available: {e}", file=sys.stderr)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')
print(f"INDEX: DJANGO_SETTINGS_MODULE set to: {os.environ.get('DJANGO_SETTINGS_MODULE')}", file=sys.stderr)

try:
    print("INDEX: Importing Django", file=sys.stderr)
    # Import Django and setup
    import django
    print(f"INDEX: Django version: {django.VERSION}", file=sys.stderr)

    print("INDEX: Calling django.setup()", file=sys.stderr)
    django.setup()
    print("INDEX: Django setup successful", file=sys.stderr)

    # Import the WSGI application
    print("INDEX: Importing WSGI application", file=sys.stderr)
    from Portfolio.wsgi import application
    print("INDEX: WSGI application imported successfully", file=sys.stderr)

except Exception as e:
    print(f"INDEX: CRITICAL ERROR during setup: {e}", file=sys.stderr)
    print("INDEX: Full traceback:", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    raise

# For Vercel, we need to export the app
print("INDEX: Exporting app for Vercel", file=sys.stderr)
app = application