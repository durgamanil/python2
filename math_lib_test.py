# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:55:47 2020

@author: Onyx1
"""

import math
from tkinter import *
 
def calculatePayment(amount, intRate, years) :
    amount = entAmount.get()
    intRate = entIntRate.get()
    years = entYears.get()
    interest = intRate / 100
    interest = interest / 12
    payment = (amount * interest) / (1 - (math.pow(1 / (1 + interest), years * 12)))
    #lblMonthlyPayment = Label(main, text = payment)
    #lblTotalPayment = Label(main, text = payment * 12 * years)
    return payment
 
main = Tk()
main.title("How Much?")
main.geometry('300x300')
 
lblAmount = Label(main, text = 'Amount of Purchase:')
lblAmount.grid(row = 0, column = 0, padx = 0, pady = 10)
a = StringVar()
entAmount = Entry(main, width = 20)
entAmount.grid(row = 0, column = 1)
 
lblIntRate = Label(main, text = 'Interest Rate (like 7.5):')
lblIntRate.grid(row = 1, column = 0, padx = 0, pady = 10)
entIntRate = Entry(main, width = 20)
entIntRate.grid(row = 1, column = 1)
 
lblYears = Label(main, text = 'Years to Pay:')
lblYears.grid(row = 2, column = 0, padx = 0, pady = 10)
entYears = Entry(main, width = 20)
entYears.grid(row = 2, column = 1)
 
lblMonthly = Label(main, text = 'Monthly Payment:')
lblMonthly.grid(row = 3, column = 0, padx = 0, pady = 10)
lblMonthly.bind(calculatePayment)
 
lblTotal = Label(main, text = 'Total Purchase Cost:')
lblTotal.grid(row = 4, column = 0, padx = 0, pady = 10)
 
btn = Button(main, text = 'Calculate', command = calculatePayment)
btn.grid(row = 5, column = 1)
 
main.mainloop()