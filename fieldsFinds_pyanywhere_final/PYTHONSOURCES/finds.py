#!/usr/bin/python3.8
import cgitb
import cgi
import os
import sys
import mysql.connector
print("Content-type: text/html\n")
# print(os.getcwd())
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:36:59 2019

@author: no33mis

This file creates and displays the formatted fields and crops table from the database with the
help of jinja2 templating
"""

# create a function that will connect to the database, exececute the joined finds and class
# table, loop through the rows and return the columns


def findsHtml(finds):
    conn = mysql.connector.connect(
            host= "xxx.mysql.pythonanywhere-services.com", user="xxx", password="xxx", db="xxx")
    c = conn.cursor()
    # execute the joined table
    c.execute("SELECT * FROM FINDS JOIN CLASS ON FINDS.TYPE = CLASS.TYPE")

    # get the form entry from "finds.html" and assign the elements to a list, then to a string and add it to the SQL statement
    if finds:
        input = "%' OR CLASS.PERIOD LIKE '%".join(finds)

        conn = mysql.connector.connect(
            host= "xxx.mysql.pythonanywhere-services.com", user="xxx", password="xxx", db="xxx")
        c = conn.cursor()
        c.execute(f"SELECT * FROM FINDS JOIN CLASS ON FINDS.TYPE = CLASS.TYPE WHERE CLASS.PERIOD LIKE '%{input}%'")

    ret = ''
    for row in c:
        # assign variables for approriate formatting where necessary
        TypeText = str(row[7]).lower().title().replace("_", " ")
        PeriodText = str(row[8]).lower().title().replace("_", " ")
        UseText = str(row[9]).lower().capitalize()
        NoteText = str(row[5]).lower().capitalize()

        ret = ret + \
            f'<tr><td>{str(row[0])}</td><td>{str(TypeText)}</td><td>{str(PeriodText)}</td><td>{str(UseText)}</td><td>{str(row[1])} - {str(row[2])}</td><td>{str(row[4])}</td><td>{str(NoteText)}</td></tr>\n'

    conn.close()

    return ret

