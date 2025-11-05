#!/bin/bash
# Test script for Vercel deployment
# Run this after deploying to test if the API endpoints work

if [ -z "$1" ]; then
    echo "Usage: $0 <vercel-deployment-url>"
    echo "Example: $0 https://my-django-app.vercel.app"
    exit 1
fi

BASE_URL=$1

echo "Testing Vercel deployment at: $BASE_URL"
echo "========================================="

# Test profile endpoint
echo "Testing /api/profile..."
PROFILE_RESPONSE=$(curl -s -w "HTTPSTATUS:%{http_code}" "$BASE_URL/api/profile")
PROFILE_HTTP_CODE=$(echo $PROFILE_RESPONSE | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')
PROFILE_BODY=$(echo $PROFILE_RESPONSE | sed -e 's/HTTPSTATUS:.*//g')

if [ "$PROFILE_HTTP_CODE" = "200" ]; then
    echo "✅ Profile endpoint: SUCCESS (200)"
    echo "Response preview: $(echo $PROFILE_BODY | head -c 100)..."
else
    echo "❌ Profile endpoint: FAILED ($PROFILE_HTTP_CODE)"
    echo "Response: $PROFILE_BODY"
fi

echo ""

# Test projects endpoint
echo "Testing /api/projects..."
PROJECTS_RESPONSE=$(curl -s -w "HTTPSTATUS:%{http_code}" "$BASE_URL/api/projects")
PROJECTS_HTTP_CODE=$(echo $PROJECTS_RESPONSE | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')
PROJECTS_BODY=$(echo $PROJECTS_RESPONSE | sed -e 's/HTTPSTATUS:.*//g')

if [ "$PROJECTS_HTTP_CODE" = "200" ]; then
    echo "✅ Projects endpoint: SUCCESS (200)"
    echo "Response preview: $(echo $PROJECTS_BODY | head -c 100)..."
else
    echo "❌ Projects endpoint: FAILED ($PROJECTS_HTTP_CODE)"
    echo "Response: $PROJECTS_BODY"
fi

echo ""
echo "========================================="
echo "Test complete. Check Vercel function logs for detailed error information if tests failed."
