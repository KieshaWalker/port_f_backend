#!/usr/bin/env python
"""
Debug script for Vercel deployment issues.
Run this locally to test Django configuration.
"""
import os
import sys
import traceback

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_django_setup():
    """Test Django setup and configuration"""
    print("Testing Django setup...")

    try:
        # Test environment variables
        print(f"DEBUG: {os.environ.get('DEBUG', 'not set')}")
        print(f"DJANGO_SECRET_KEY: {'set' if os.environ.get('DJANGO_SECRET_KEY') else 'not set'}")
        print(f"DB_NAME: {os.environ.get('DB_NAME', 'not set')}")
        print(f"DB_HOST: {os.environ.get('DB_HOST', 'not set')}")

        # Test Django import
        import django
        from django.conf import settings
        print(f"Django version: {django.VERSION}")

        # Configure Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings')
        django.setup()
        print("Django setup successful")

        # Test database connection
        from django.db import connection
        cursor = connection.cursor()
        print("Database connection successful")

        # Test apps
        from django.apps import apps
        print(f"Installed apps: {len(apps.get_app_configs())}")

        # Test API imports
        from api.api import api
        print("API import successful")

        return True

    except Exception as e:
        print(f"Error during Django setup: {e}")
        print("Full traceback:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_django_setup()
    sys.exit(0 if success else 1)