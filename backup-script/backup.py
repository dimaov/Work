#!/usr/bin/env python

import os
import subprocess
import boto3
import time
import ConfigParser

s3_client = boto3.client('s3')
date=time.strftime('%Y-%m-%d')
 
config = ConfigParser.ConfigParser()
config.read("/etc/backup.conf")

###find out hostname
f  = os.popen('hostname').read()
hostname = f.rstrip('\n')

###general vars

gen_enable = config.get('general', 'enabled')
backetname = config.get('general', 's3backet')
dirs = config.get('general', 'dirs')
arch_name = '%s-archive-%s.tar.gz' %  (hostname,date)

###mysql vars

mysql_enabled = config.get('mysql', 'enabled')
username = config.get('mysql', 'user')
password = config.get('mysql', 'password')
dump_name = '%s-all-databases-%s.sql' % (hostname,date)

###postgres vars

postg_enabled = config.get('postgres', 'enabled')
user = config.get('postgres', 'user')
postg_dump_name = '%s-postg-databases-%s.sql' % (hostname,date)

###tasks section

if gen_enable:
   from subprocess import Popen, PIPE
   Popen('tar  -czvf %s  %s' %  (arch_name,dirs) , shell=True, stdout=PIPE).communicate()
   s3_client.upload_file('%s' % arch_name, backetname, '%s/%s' % (hostname,arch_name))
   os.remove(arch_name)

if mysql_enabled: 
   from subprocess import Popen, PIPE
   Popen('mysqldump -u %s --password=%s --max_allowed_packet=512M --all-databases >> %s' % (username,password,dump_name) , shell=True, stdout=PIPE).communicate()
   s3_client.upload_file('%s' % dump_name, backetname, '%s/%s' % (hostname,dump_name))
   os.remove(dump_name)

if postg_enabled:
   from subprocess import Popen, PIPE
   Popen('pg_dumpall -U %s > %s' % (user,postg_dump_name), shell=True, stdout=PIPE).communicate()
   s3_client.upload_file('%s' % postg_dump_name, backetname, '%s/%s' % (hostname,postg_dump_name))
   os.remove(postg_dump_name)


