sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepik;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'pass123';"
mysql -uroot -e "GRANT ALL ON stepik.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
