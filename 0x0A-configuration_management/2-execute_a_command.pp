# This kills a process
exec {'kill':
  command => 'pkill killmenow',
  path    => ['usr/bin', 'usr/sbin']
}
