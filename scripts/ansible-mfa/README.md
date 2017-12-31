# Project Title

Ansible against servers with MFA enabled

## Getting Started

This script allows you to manipulate servers with MFA enabled via ansible-playbooks

### Prerequisites

pexpect python module have to be inatslled

```
pip install pexpect
```
ansible have to be installed. For installing ansible see oficial documentation http://docs.ansible.com/ansible/latest/intro_installation.html

### Installing

Clone repositary and use ansible.mfa.py script. 
Change totp = pyotp.TOTP('XXXXX') Where XXXXX MFA token for user that ansible will be run from

```
git clone https://dimaov@bitbucket.org/taxesforexpats/devops.git
cd devops
cd ansible-mfa

```

## Running the tests

create playbook called test.yml in the directory where script is located with content:


```
---
- hosts: all
  serial: 1
  tasks:
  - name: ping
    ping:
```

Then run a script. You have to pass playbook name as parameter to this script. Also you can pass additional parameters in the same way as it passing to ansible-playbook command

```
./ansible_mfa.py test.yml -i inventory -e "foo=bar"
```

## Authors

Dmitriy Ovchinnikov
Alex Schelkanov
