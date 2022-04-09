#/bin/sh
source ./venv/bin/activate
gunicorn main:app --daemon --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 --access-logfile access.log
deactivate