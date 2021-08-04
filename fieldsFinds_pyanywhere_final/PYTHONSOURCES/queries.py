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

This file creates and displays the queries according to the user inputs with the
help of jinja2 templating
"""
# import the necessary packages for database connection and jinja2 templating, and enable the CGI script
# cgitb.enable()

# open and assign the pw file for the database
# with open("../../wTh467", 'r') as pwf:
#     pw = pwf.read().strip()

# create a function that will create the form, assign the user inputs and include
# them into the SQL query. It then loops through the rows and outputs the requestes
# elements only


def findsQuery(find):
    ret = " "
    # assign a form variable and get the user input from "queries.html" to display
    # only the finds that lie within the requested field
    if find:

        conn = mysql.connector.connect(
            host="no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
        c = conn.cursor()
        c.execute(
            f'SELECT * FROM FINDS, CLASS, FIELDS WHERE (FINDS.XCOORD BETWEEN FIELDS.LOWX AND FIELDS.HIX) AND (FINDS.YCOORD BETWEEN FIELDS.LOWY AND FIELDS.HIY) AND (CLASS.TYPE = FINDS.TYPE) and (FIELDS.FIELD_ID = {find})')

        ret = ''
        for row in c:
            # assign variables for approriate formatting where necessary
            TypeText = str(row[7]).lower().title().replace("_", " ")
            PeriodText = str(row[8]).lower().title().replace("_", " ")
            UseText = str(row[9]).lower().capitalize()

            ret = ret + \
                f'<tr><td>{find}</td><td>{str(row[0])}</td><td>{str(TypeText)}</td><td>{str(PeriodText)}</td><td>{str(UseText)}</td></tr>'

        conn.close()

    return ret

# create a function that will create the form, assign the user inputs and include
# them into the SQL query. It then loops through the rows and outputs the requested
# elements only


def farmerQuery(farm):
    ret = " "
    # assign a form variable and get the user input from "queries.html" to display
    # only the finds that lie within the requested field
    if farm:

        conn = mysql.connector.connect(
            host="no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
        c = conn.cursor()
        c.execute(
            f"SELECT SUM(AREA) FROM FIELDS WHERE (FIELDS.OWNER LIKE '%{farm}%')")

        ret = ''
        for row in c:
            # assign variables for approriate formatting where necessary
            farmEr = "Farmer " + farm.lower().capitalize()
            ret = ret + f'<tr><td>{farmEr}</td><td>{str(row[0])}</td></tr>'

        conn.close()

    return ret

# create a function that will create the form, assign the user inputs and include
# them into the SQL query. It then loops through the rows and outputs the requested
# elements only


def typeQuery(type):
    ret = " "
    # assign a form variable and get the user input from "queries.html" to display
    # only the finds that lie within the requested field
    if type:

        conn = mysql.connector.connect(
            host="no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
        c = conn.cursor()
        c.execute(
            f"SELECT AVG (DEPTH) FROM FINDS JOIN CLASS ON FINDS.TYPE = CLASS.TYPE WHERE (CLASS.NAME LIKE '%{type}%')")

        ret = ''
        for row in c:
            # assign variables for approriate formatting where necessary
            typeEr = type.lower().title().replace("_", " ")
            RoundDepth = str(round(row[0], 2))

            ret = ret + f'<tr><td>{typeEr}</td><td>{RoundDepth}</td></tr>'

        conn.close()

    return ret

