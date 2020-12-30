# 系统设置
apt -y update
apt -y upgrade
# 装依赖
apt -y install git zsh curl ufw supervisor nginx mysql-server
pip3 install jinja2 flask gunicorn PyMySQL SQLAlchemy

# 删掉 nginx default 设置
rm -f /etc/nginx/sites-enabled/default
rm -f /etc/nginx/sites-available/default

# 建立一个软连接
cp forum-flask.conf /etc/supervisor/conf.d/forum-flask.conf
# 不要在 sites-available 里面放任何东西
cp forum-flask.nginx /etc/nginx/sites-enabled/forum-flask

# 重启服务器
service supervisor restart
service nginx restart

echo 'deploy success'