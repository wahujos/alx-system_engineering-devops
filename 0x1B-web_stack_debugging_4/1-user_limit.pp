# change the hard and soft limit of the holberton user
# the said configurations can be found in /etc/security/limits.conf

exec {
command => 'sed -i "/^holberton hard/s/5/5000/" /etc/security/limits/conf'
path    => '/usr/local/bin/:/bin/'
}
exec {
command => 'sed -i "/^holberton soft/s/4/5000/" /etc/security/limits/conf'
path    => '/usr/local/bin/:/bin/'
}
