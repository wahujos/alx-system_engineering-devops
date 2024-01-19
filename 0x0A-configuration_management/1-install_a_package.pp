# install a package flask using Puppet

package { 'flask':
  ensure  => 'installed',
  require => Exec['pip3 install flask']
}
exec { 'pip3 install flask':
  command => '/usr/bin/pip3 install flask 2.1.0'
}
