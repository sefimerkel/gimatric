sudo chown -R sefi:www-data /srv/www/gimatric
sudo cp gimatric.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start gimatric
sudo systemctl enable gimatric
sudo cp nginx.server  /etc/nginx/sites-available/gimatric
if ! [ -f /etc/nginx/sites-enabled/gimatric ]; then
    sudo ln -s /etc/nginx/sites-available/gimatric  /etc/nginx/sites-enabled
fi    
sudo nginx -t
sudo systemctl restart nginx
sudo systemctl status gimatric | tee