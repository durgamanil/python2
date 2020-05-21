# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:23:24 2020

@author: Onyx1
"""
import pygame, sys
from pygame.locals import *
pygame.init()
displaysurf=pygame.display.set_mode((1024,800))
pygame.display.set_caption('Hello world!!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
