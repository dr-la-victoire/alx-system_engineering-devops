# This is a puppet manifest that kills a process named killmenow

exec {'kills killmenow':
  command => pkill killmenow
}
