# test.

exec { 'fix':
  command  => 'sudo sed -i "s/-n */-n 5000000/g" /etc/default/nginx && sudo service nginx restart',
  provider => shell
}
