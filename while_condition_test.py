# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:46:35 2020

@author: Onyx1
"""

card_deck = [12,15,8,10,14,16,6,8]
hand = []

while sum(hand) <=17 :
    hand.append(card_deck.pop())

print(hand)