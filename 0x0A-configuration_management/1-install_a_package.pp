# This puppet mainfest installs flask from pip3

package { 'flask':
  ensure   => 'installed',
  version  => '2.1.0',
  provider => 'pip3'
}
