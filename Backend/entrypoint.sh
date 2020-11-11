#!/bin/sh
if /app/wait-for-it.sh db::3306 --strict --timeout=300 
then
    if [ ! "$(ls -A /app/migrations/)" ]
    then
        flask db init
        flask db migrate -m "Database init"
        flask db upgrade
        python3 -m app.manage init_admin
    fi
    gunicorn --reload --bind 0.0.0.0:5000 --capture-output --enable-stdio-inheritance --timeout 3000 app.wsgi:app
fi
