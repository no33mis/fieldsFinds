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

# create a function that will connect to the database, exececute the joined fields and crops
# table, loop through the rows and return the columns


def fieldsHtml(field):

    conn = mysql.connector.connect(
        host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
    c = conn.cursor()
    # execute the joined table
    c.execute("SELECT * FROM FIELDS JOIN CROPS ON FIELDS.CROP = CROPS.CROP")
    # get the form entry from "fields.html" and assign the elements to a list, then to a string and add it to the SQL statement

    if field:

        input = "%' OR CROPS.NAME LIKE '%".join(field)

        conn = mysql.connector.connect(
            host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
        c = conn.cursor()
        c.execute(f"SELECT * FROM FIELDS JOIN CROPS ON FIELDS.CROP = CROPS.CROP WHERE CROPS.NAME LIKE '{input}'")

    ret = ''
    for row in c:
        # assign variables for approriate formatting where necessary
        SoS = row[10].strftime("%d / %m - %B")
        EoS = row[11].strftime("%d / %m - %B")

        FarmerText = str(row[6]).lower().title()
        CropText = str(row[9]).lower().title()

        ret = ret + f'<tr><td>{str(row[0])}</td><td>{str(FarmerText)}</td><td>{str(round(row[5],2))}</td><td>{str(row[1])} - {str(row[2])} - {str(row[3])} - {str(row[4])}</td><td>{str(CropText)}</td><td>{str(SoS)}</td><td>{str(EoS)}</td></tr>\n'

    conn.close()

    return ret


