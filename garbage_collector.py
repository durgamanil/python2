# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 00:09:18 2020

@author: Onyx1
"""

import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
