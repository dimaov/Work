#!/usr/bin/env python
import string
from random import *
characters = string.ascii_letters + string.digits
password =  "".join(choice(characters) for x in range(randint(15, 17)))
import sys


print password
