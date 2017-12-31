#!/usr/bin/env python
import pexpect
import pyotp
import os
import sys
totp = pyotp.TOTP('XMVEA76DMSB2DD4UI5ZLCAQJG4')
list_opts =  ' '.join(sys.argv[1:])
print list_opts
child = pexpect.spawn('ansible-playbook  %s'  % list_opts, logfile=sys.stdout)
#otp = totp.now()
while True:
	child.expect("Verification code: ")
	otp = totp.now()
	child.sendline('%s\n' % otp)
	if  'PLAY RECAP' in child.readline():
        	print child.readline()
        	break
child.expect(pexpect.EOF, timeout=5)
