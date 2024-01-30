#  automate the task of creating a custom HTTP header response, but with Puppet.
#update apt package
exec {'update_apt_store':
  command => '/usr/bin/apt-get update',
}
#Install nginx package
packege {'nginx':
  ensure  => 'present',
  require => Exce['update_apt_store'],
}
# Add a line to Nginx configuration
file_line {'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match => Exec['restart_nginx'],
}
#Restart nginx
exec {'restart_nginx':
  commad      => '/usr/sbin/service nginx resart',
  refreshonly => true,
}
