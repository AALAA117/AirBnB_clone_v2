#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

#Install Nginx if it not already installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

#create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared /data/web_static/current

#create a fake html
echo "<html><head><title>Test Page</title></head><body>This is a test page.</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#Create a symbolic link or recreate
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content
config_file="/etc/nginx/sites-enabled/default"
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' $config_file
sudo service nginx restart
