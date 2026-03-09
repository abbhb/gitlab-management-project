#!/bin/bash
# Pre-release hook for BlueKing PaaS deployment
# This script runs before the application is deployed

set -e

echo "Running pre-release hook..."

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Pre-release hook completed successfully."
