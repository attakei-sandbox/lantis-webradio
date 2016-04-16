FROM python:3.5.1-onbuild

VOLUME /var/lib/lantis/tmp
VOLUME /var/lib/lantis/data

ENTRYPOINT [ "python", "main.py" ]
