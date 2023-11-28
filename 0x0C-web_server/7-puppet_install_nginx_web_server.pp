#automating work using puppet

packege { 'ngnix':
  ensure => installed,
}
file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites_enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.github.com/bm-197 permanent;',
}

file { '/var/www/html/index.html':
  content => 'Hello world!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
