#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx

#create necessary directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#create a fake html
echo "<html><head><title>Test Page</title></head><body>This is a test page.</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#Create a symbolic link or recreate
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content
config_file="/etc/nginx/sites-enabled/default"
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' $config_file
sudo service nginx restart
