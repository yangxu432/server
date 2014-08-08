#!/bin/sh
source ../ENV/bin/activate
cd sci-wms
python manage.py runserver 0.0.0.0:8000
