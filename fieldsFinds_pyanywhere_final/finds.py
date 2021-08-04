#!/usr/bin/python3.8
from jinja2 import Environment, FileSystemLoader
import cgitb
import cgi
import os
import sys
import mysql.connector
from flask import Flask, render_template, request, redirect
print("Content-type: text/html\n")
# print(os.getcwd())
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:36:59 2019

@author: no33mis

This file creates and displays the formatted fields and crops table from the database with the
help of jinja2 templating
"""

# start flask and set config
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# set the routing for the main landing page
@app.route("/")
def print_html():
    inpFinds = findsHtml(None)
    return render_template('findsTemp.html', finds=inpFinds)

@app.route("/filter", methods = ["POST"])
def filter():
    finds = request.form.getlist("find")
    inpFinds = findsHtml(finds)
    return render_template('findsTemp.html', finds=inpFinds)

# create a function that will connect to the database, exececute the joined finds and class
# table, loop through the rows and return the columns


def findsHtml(finds):
    conn = mysql.connector.connect(
            host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
    c = conn.cursor()
    # execute the joined table
    c.execute("SELECT * FROM FINDS JOIN CLASS ON FINDS.TYPE = CLASS.TYPE")

    # get the form entry from "finds.html" and assign the elements to a list, then to a string and add it to the SQL statement
    if finds:
        input = "%' OR CLASS.PERIOD LIKE '%".join(finds)

        conn = mysql.connector.connect(
            host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
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


# call the main function
if __name__ == '__main__':
    app.run(debug=True)
    print_html()
