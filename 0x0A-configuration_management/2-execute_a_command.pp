# This kills a process
exec {'killmenow':
  command => 'pkill'
}
