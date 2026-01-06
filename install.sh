#!/bin/bash

# Update and install required packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y vlc
sudo apt install -y python3-pip
sudo apt install -y python3-pygame
sudo apt install -y python3-vlc
sudo apt install -y python3-flask
sudo apt install -y python3-flask-cors
sudo apt install -y gunicorn
sudo apt install -y tmux
sudo apt install -y neovim
sudo apt install -y iptables-persistent

# Enable VNC
sudo raspi-config nonint do_vnc 0

# Setup Ports
# Open port 80 for web server, link to port 12413
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 12413

# Open port 80 for internal access
sudo iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-port 12413

# Save iptables rules
sudo netfilter-persistent save

# Launch the server and say to check
cd Server-Template

echo "Starting the server with Gunicorn..."
./launch.sh
