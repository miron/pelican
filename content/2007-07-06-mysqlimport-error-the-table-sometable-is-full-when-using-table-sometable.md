Title: mysqlimport: Error: table full when using table
Date: 2007-07-06
Category: Linux
Tags: mysql gentoo full
Summary: full tables aren't fun

If this error drives you mad on Gentoo, change this line in your /etc/mysql/my.cnf (if you use inoDB):

`innodb_data_file_path = ibdata1:10M:autoextend:max:128M`

and delete the :max:128M part or raise it up to your liking.
