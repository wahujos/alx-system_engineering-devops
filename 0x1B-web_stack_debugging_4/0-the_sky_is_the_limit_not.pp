# Backup the original nginx configuration file
file { '/etc/default/nginx_backup':
  ensure => 'file',
  source => '/etc/default/nginx',
}
# Update the ulimit in the nginx configuration file
exec { 'update-ulimit':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  unless  => '/bin/grep -q "ulimit -n 4096" /etc/default/nginx',
  notify  => Exec['restart-nginx'],
}
# Restart nginx only if the configuration is changed
exec { 'restart-nginx':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
  subscribe   => Exec['update-ulimit'],
}
