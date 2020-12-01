#!/bin/bash
python3 download_data.py
gunicorn api:app --workers 4 --bind 0.0.0.0:5000