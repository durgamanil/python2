# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:48:22 2020

@author: Onyx1
"""

import mysql.connector

def connect():
    #connect to mysql database
    try:
        conn=mysql.connector.connect(
                host='localhost',
                database='db01',
                user='root',
                password='admin'
                )
        if conn.is_connected():
            print("connected to MYSQL database\n")
    
    except  Error as e:
        print(e)
        
    