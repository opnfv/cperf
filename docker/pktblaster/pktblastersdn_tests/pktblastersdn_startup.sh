#!/bin/bash

/etc/init.d/tomcat6 start
/usr/bin/mysqld_safe > /dev/null 2>&1 &
echo "startup...."
