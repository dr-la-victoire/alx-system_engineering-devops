# A Puppet manifest that fixes the Apache error for the web stack project

$file_to_edit = '/var/www/html/wp-settings.php'

file_line { 'replace_phpp_with_php':
  path  => $file_to_edit,
  line  => 'php',
  match => 'phpp'
}

