# We are using the apache benchmark to test our server during pressure
# We are seeking to change the ulimit since this determines the number
# of files that can be open at a particular time

exec {
command => '/bin/sed -i "s/15/10240/" /etc/default/nginx',
path    => '/usr/local/bin/:/bin/'
}
# restart the nginx server
exec {
command => '/etc/init.d/nginx restart',
path    => '/etc/init.d/',
}
