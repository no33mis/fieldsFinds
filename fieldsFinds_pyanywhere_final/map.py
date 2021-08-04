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

This file will draw a map using the information from the database with the help
of SVG and jinja2 templating
"""

# start flask and set config
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# set the routing for the main landing page
@app.route("/")
def print_html():
    inpGrid = createGrid()
    inpRect = createRect(None)
    inpRectText = createRectText()
    inpCircle = createCircle(None)
    inpInfoR = infoBoxRect()
    inpInfoC = infoBoxCircle()

    return render_template('mapTemp.html', grid=inpGrid, rect=inpRect, text=inpRectText,
                      circle=inpCircle, infoRect=inpInfoR, infoCircle=inpInfoC)


# set the routing for the filters
@app.route("/filter", methods = ["POST"])
def filterMap():

    area = request.form.get("AreaRange")
    depth = request.form.get("FindDepth")

    inpGrid = createGrid()
    inpRect = createRect(area)
    inpRectText = createRectText()
    inpCircle = createCircle(depth)
    inpInfoR = infoBoxRect()
    inpInfoC = infoBoxCircle()

    return render_template('mapTemp.html', grid=inpGrid, rect=inpRect, text=inpRectText,
                      circle=inpCircle, infoRect=inpInfoR, infoCircle=inpInfoC)


# with open("../dhue742.txt",'r') as pwf:
#     pw = pwf.read().strip()


# create a function to display a 16 x 16 SVG path grid with the help of a range loop


def createGrid():
    ret = ''
    for j in range(17):
        ret = ret + \
            f'<path stroke="grey" stroke-width="0.02" d="M{str(j)} 0 v16"/>\n<path stroke="grey" stroke-width="0.02" d="M0 {str(j)} H16"/>\n'

    return ret

# create a function that will connect to the database, exececute the fields table,
# loop through the rows and return the rectangles in different colours according
# to their crop type


def createRect(area):

    conn = mysql.connector.connect(
        host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
    c = conn.cursor()
    c.execute("SELECT * FROM FIELDS")

    # assign a form variable and get the user input from "map.html" to Display
    # only the fields with larger areas

    if area:

        conn = mysql.connector.connect(
        host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
        c = conn.cursor()
        c.execute("SELECT * FROM FIELDS WHERE AREA > " + area)

    # create empty strings and loop through the rows
    ret1 = ''
    ret2 = ''
    ret3 = ''
    ret4 = ''
    ret5 = ''
    ret6 = ''
    for row in c:
        # for turnips
        if str(row[7]) == "1":
            ret1 = ret1 + \
                f'<rect class="hover infoBox{str(row[0])}" x="{str(row[1])}" + y="{str(16-row[4])}" width="{str(row[3]-row[1])}" height="{str(row[4]-row[2])}" fill="#9370DB" stroke="black" stroke-width="0.03" fill-opacity="0.4" />\n '

    # for oil seed rape
        elif str(row[7]) == "2":
            ret2 = ret2 + \
                f'<rect class="hover infoBox{str(row[0])}" x="{str(row[1])}" + y="{str(16-row[4])}" width="{str(row[3]-row[1])}" height="{str(row[4]-row[2])}" fill="#FFD700" stroke="black" stroke-width="0.03" fill-opacity="0.4" />\n'

    # for strawberries
        elif str(row[7]) == "3":
            ret3 = ret3 + \
                f'<rect class="hover infoBox{str(row[0])}" x="{str(row[1])}" + y="{str(16-row[4])}" width="{str(row[3]-row[1])}" height="{str(row[4]-row[2])}" fill="#FF6347" stroke="black" stroke-width="0.03" fill-opacity="0.4" />\n'

    # for peas
        elif str(row[7]) == "4":
            ret4 = ret4 + \
                f'<rect class="hover infoBox{str(row[0])}" x="{str(row[1])}" + y="{str(16-row[4])}" width="{str(row[3]-row[1])}" height="{str(row[4]-row[2])}" fill="#2E8B57" stroke="black" stroke-width="0.03" fill-opacity="0.4" />\n'

    # for potatoes
        elif str(row[7]) == "5":
            ret5 = ret5 + \
                f'<rect class="hover infoBox{str(row[0])}" x="{str(row[1])}" + y="{str(16-row[4])}" width="{str(row[3]-row[1])}" height="{str(row[4]-row[2])}" fill="#A0522D" stroke="black" stroke-width="0.03" fill-opacity="0.4" />\n'

    # for other fields if there would be any
        else:
            ret6 = ret6 + \
                f'<rect x="{str(row[1])}" + y="{str(16-row[4])}" width="{str(row[3]-row[1])}" height="{str(row[4]-row[2])}" fill="grey" stroke="black" stroke-width="0.03" fill-opacity="0.2" />\n'

    conn.close()

    ret = ret1 + ret2 + ret3 + ret4 + ret5 + ret6

    return ret

# create a function that will connect to the database, exececute the fields table,
# loop through the rows and return the fields ID's


def createRectText():

    conn = mysql.connector.connect(
        host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
    c = conn.cursor()
    c.execute("SELECT * FROM FIELDS")

    # assign a form variable and get the user input from "map.html" to Display
    # only the field ID texts with larger areas
    form = cgi.FieldStorage()
    if form.getvalue("AreaRange"):
        area = form.getvalue("AreaRange")

        conn = mysql.connector.connect(
            host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
        c = conn.cursor()
        c.execute("SELECT * FROM FIELDS WHERE AREA > " + area)

    ret = ''
    for row in c:
        # define variables to place the information onto the right position
        CENT_X = str((row[3]+row[1])/2-0.3)
        CENT_Y = str(16-(row[4]+row[2])/2+0.3)

        ret = ret + \
            f'<text class="txt1" x="{str(CENT_X)}" y="{str(CENT_Y)}" font-family="Arial Black" font-size="1" fill="black">{str(row[0])}</text>\n'

    conn.close()

    return ret

# create a function that will connect to the database, exececute the finds table,
# loop through the rows and return the SVG circles as well as the find ID's


def createCircle(depth):

    conn = mysql.connector.connect(
        host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
    c = conn.cursor()
    c.execute("SELECT * FROM FINDS")

    # assign a form variable and get the user input from "map.html" to Display
    # only the finds with larger depths than the input
    if depth:

        conn = mysql.connector.connect(
            host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
        c = conn.cursor()
        c.execute("SELECT * FROM FINDS WHERE DEPTH > " + depth)

    ret1 = ''
    ret2 = ''
    for row in c:
        ret1 = ret1 + \
            f'<circle class="circle circleInfo{str(row[0])}" cx="{str(row[1])}" cy="{str(16-row[2])}" r="0.4" fill="#B0C4DE" stroke="black" stroke-width="0.04" />\n'

        ret2 = ret2 + \
            f'<text class="txt2 circle_text" x="{str(row[1]-.175)}" y="{str(16-row[2]+.175)}" font-family="Arial" font-size="0.6" fill="black">{str(row[0])}</text>\n'

    conn.close()

    ret = ret1 + ret2

    return ret

# create a function that will connect to the database, join the fields and crops,
# loop through the rows and return the information for the info boxes and queries


def infoBoxRect():

    conn = mysql.connector.connect(
        host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM FIELDS JOIN CROPS ON FIELDS.CROP = CROPS.CROP")

    ret = ''
    for row in c:
        # assign variables for approriate formatting where necessary
        SoS = row[10].strftime("%B %d")
        EoS = row[11].strftime("%B %d")

        FarmerText = str(row[6]).lower().title()
        CropText = str(row[9]).lower().title()

        ret = ret + f'<div class="hoverInfo" id="field{str(row[0])}">\n <span class="helper"></span>\n <div>\n <div class="infoButton" id="fieldbutton{str(row[0])}">&times;</div>\n <h3> Field #{str(row[0])} </h3> <p> Farmer Name: {str(FarmerText)} <br> Field Area: {str(round(row[5],2))} ha <br> Crop Type: {str(CropText)} <br> Start of Season: {str(SoS)} <br> End of Season: {str(EoS)} </p>\n </div>\n </div>\n'

    conn.close()

    return ret

# create a function that will connect to the database, join the finds and classes,
# loop through the rows and return the information for the info boxes


def infoBoxCircle():

    conn = mysql.connector.connect(
        host= "no33mis.mysql.pythonanywhere-services.com", user="no33mis", password="dhsgt@672!", db="no33mis$fieldsFinds")
    c = conn.cursor()
    c.execute(
        "SELECT * FROM FINDS JOIN CLASS ON FINDS.TYPE = CLASS.TYPE")

    ret = ''
    for row in c:
        # assign variables for approriate formatting where necessary

        TypeText = str(row[7]).lower().title().replace("_", " ")
        PeriodText = str(row[8]).lower().title().replace("_", " ")
        UseText = str(row[9]).lower().capitalize()
        NoteText = str(row[5]).lower().capitalize()

        ret = ret + f'<div class="hoverInfo" id="find{str(row[0])}">\n <span class="helper"></span>\n <div>\n <div class="infoButton" id="findbutton{str(row[0])}">&times;</div>\n <h3> Find #{str(row[0])} </h3> <p> Find Type: {str(TypeText)} <br> Period: {str(PeriodText)} <br> Use: {str(UseText)} <br> Depth: {str(row[4])} meters <br> Field Notes: {str(NoteText)} </p>\n </div>\n </div>\n'

    conn.close()

    return ret


# call the main function
if __name__ == '__main__':
    app.run(debug=True)
    print_html()


