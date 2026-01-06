#!/bin/bash

FILE_FOUND=$(find . -maxdepth 1 -name "*.service" | head -n 1)
echo "Service file found: $FILE_FOUND"
SERVICE_NAME=$(basename "$FILE_FOUND")
echo "Service name extracted: $SERVICE_NAME"
WHOAMI=$(whoami)
echo "Current user: $WHOAMI"
SERVICE_LOCATION="/home/$WHOAMI/Server-Template/$SERVICE_NAME"
echo "Service location set to: $SERVICE_LOCATION"

sudo ln -s $SERVICE_LOCATION /etc/systemd/system/$SERVICE_NAME
sudo systemctl daemon-reload
sudo systemctl enable bespoke-reality.service
sudo systemctl start bespoke-reality.service
sudo systemctl status bespoke-reality.service

echo "Bespoke Reality service has been made permanent and started."
