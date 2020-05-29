# Test

exec { 'fix':
  command  => 'sudo sed -i "s/nofile */nofile 50000/g" /etc/security/limits.conf',
  provider => 'shell'
}
