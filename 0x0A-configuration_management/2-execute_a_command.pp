#make file
exec { 'kill':
  command => 'pkill killmenow',
  path    => '/usr/bin'
}
