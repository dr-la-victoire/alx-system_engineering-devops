# A Puppet manifest that fixes the Apache error for the web stack project

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}

