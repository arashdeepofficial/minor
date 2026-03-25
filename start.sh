#!/usr/bin/env bash

gunicorn event_manager.wsgi:application
