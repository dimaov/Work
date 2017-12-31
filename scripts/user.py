#!/usr/bin/env python
import json, boto3
import string

# Connect to IAM with boto
iam = boto3.client('iam')

# Create user
iam.create_user(UserName='awsuser')

# Apply policy to created user
response = iam.attach_user_policy(
    UserName='awsuser',
    PolicyArn='arn:aws:iam::aws:policy/CloudWatchLogsReadOnlyAccess'
)

from random import *
characters = string.ascii_letters  + string.digits
password =  "".join(choice(characters) for x in range(randint(15, 16)))


from subprocess import Popen, PIPE
Popen('aws iam create-login-profile --user-name awsuser --password "%s" ' % password, shell=True, stdout=PIPE).communicate()

import sys
sys.stdout = open("/root/file.xt", "a")
print "awsuser"
print password

