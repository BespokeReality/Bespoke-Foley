#!/bin/bash

GUNICORN_CONF=./src/gunicorn.conf.py
GUNICORN_PID=./src/gunicorn.pid

# Create a tmux session called "Bespoke"
tmux new-session -d -s Bespoke

# Run the gunicorn server in the "Bespoke" session
# gunicorn --reload -c $GUNICORN_CONF --pid $GUNICORN_PID src.app:app
tmux send-keys -t Bespoke "gunicorn --reload -c $GUNICORN_CONF --pid $GUNICORN_PID src.app:app" C-m
