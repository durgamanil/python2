# -*- coding: utf-8 -*-
"""

Points	Prize
1 - 50	wooden rabbit
51 - 150	no prize
151 - 180	wafer-thin mint
181 - 200	penguin
"""

num=int(input("enter a number"))
if num > 1 and num <=50 :
    print("Congratulations! You won a wooden rabbit!")
elif num > 50 and num <=150:
    print("Oh dear, no prize this time.")
elif num > 150 and num <=180:
    print("Congratulations! You won a wafer-thin mint!")
elif num > 180 and num <=200:
    print("Congratulations! You won a penguin")
else :
     print("Oh dear, no prize this time.")
    
    
    