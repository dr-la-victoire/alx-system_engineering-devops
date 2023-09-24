# This manifest enables connection to SSH without password auth

file {'~/.ssh/config':
  ensure  => 'present',
  content => "Host myserver 
	      HostName 100.26.231.31
	      User ubuntu
	      IdentityFile ~/.ssh/school"
}
