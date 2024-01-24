#!/usr/bin/env bash
# client configuration file with puppet

file_line {'remove password authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line {'File Identity':
  path => '/etc/ssh/ssh_config',
  line => 'Identity ~/.ssh/school',
}
