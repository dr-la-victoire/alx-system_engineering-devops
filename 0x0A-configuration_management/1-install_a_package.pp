# This file installs a package (Flask) with pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
