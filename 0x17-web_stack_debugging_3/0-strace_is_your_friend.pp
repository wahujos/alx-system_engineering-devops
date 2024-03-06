# correcting the 500 error on the apache sever

exec {'fixing-apache-server':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
