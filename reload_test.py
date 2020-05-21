# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 22:47:15 2020

@author: Onyx1
"""

import time
from imp import reload
import module1
print("entering into module1 program\n")
time.sleep(30)
reload(module1)
print("this is the after first reload of the program testing\n")
time.sleep(30)
reload(module1)
print("this is the last line of the program ..second reload process after line\n")


