#!/usr/bin/env bash
set -e
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
exec python -m gunicorn --chdir search tsakorpus.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2
