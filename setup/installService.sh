
sudo chown -R sefi:www-data /srv/www/gimatric
sudo cp /srv/www/gimatric/setup/gimatric.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl restart gimatric
sudo systemctl enable gimatric
sudo cp /srv/www/gimatric/setup/nginx.server  /etc/nginx/sites-available/gimatric
if ! [ -f /etc/nginx/sites-enabled/gimatric ]; then
    sudo ln -s /etc/nginx/sites-available/gimatric  /etc/nginx/sites-enabled
fi    
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl status gimatric | tee
