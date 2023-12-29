# Trying to connect to a server without password
# Using puppet to try to configure to achieve this

exec {'~/.ssh/school':
	command => cp ~/.ssh/school.pub ~/.ssh/authorized_keys 
}
