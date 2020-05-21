# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:01:13 2019

@author: anil durgam
"""
import os
  
html = ""
def table(x):
	global html
	""" Create table with data in a multiline
	string as first argument x)"""
	html = "<!-- table -->"
	html += "<table border=1>"
	for line in x.splitlines():
		for n in line.split():
			html += f"<td>{n}</td>"
		html += "<tr>"
	html += "</table>"
	return html
 
def create(a):
	tab = table(text.get("1.0", tk.END))
	text.delete("1.0", tk.END)
	text.insert("1.0", tab)
	label['text'] = "Now you can copy the html code for the table (ctrl + a)"
 
def save_html():
	if html != "":
		with open("table.html", "w") as file:
			file.write(text.get("1.0", tk.END))
 
def show_html():
	if os.path.exists("table.html"):
		os.startfile("table.html")
 
def convert_to_html():
	html = table(text.get("1.0",tk.END))
	clear()
	text.insert("1.0", html)
 
def clear():
	text.delete("1.0", tk.END)
 
import tkinter as tk
root = tk.Tk()
root.title("Html table converter")
label = tk.Label(root, text="Insert data here separated by space and press Ctrl+c to convert to html table:")
label.pack()
text = tk.Text(root)
text.pack()
text.bind("<Control-c>", create)
text.focus()
# create a toplevel menu 
menubar = tk.Menu(root)
menubar.add_command(label="Convert - crtl+c |", command=convert_to_html)
menubar.add_command(label="Save  |", command=save_html)
menubar.add_command(label="Show  |", command=show_html)
menubar.add_command(label="Clear screen  |", command=clear)
# display the menu
root.config(menu=menubar)
root.mainloop()