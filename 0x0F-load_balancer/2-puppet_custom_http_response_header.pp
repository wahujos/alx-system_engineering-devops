# creating a custom HTTP header response, but with Puppet
#Ensure package is installed
package {'nginx':
  ensure => installed,
}
#Add the header to the nginx configuration using inline template
file {'/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => @(EOT),
server {
  listen 80 default_server;
  listen [::]:80 default_server;

  server_name _;
  add_header X-Served-By <%= @hostname %>;
}
EOT
  notify  => Service['nginx'],
}
#Ensure the nginx service is running
service {'nginx':
  ensure => running,
  enable => true,
}
