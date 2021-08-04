#!/usr/bin/python3.8
from flask import Flask, render_template, request, redirect
import PYTHONSOURCES
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

# start flask and set config
app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True

# set the routing for the main landing page
@app.route("/")
def main():
    return render_template('main.html')

@app.route("/legend")
def legend():
    return render_template('map_legend.html')


@app.route("/map")
def printMap():
    inpGrid = PYTHONSOURCES.createGrid()
    inpRect = PYTHONSOURCES.createRect(None)
    inpRectText = PYTHONSOURCES.createRectText()
    inpCircle = PYTHONSOURCES.createCircle(None)
    inpInfoR = PYTHONSOURCES.infoBoxRect()
    inpInfoC = PYTHONSOURCES.infoBoxCircle()

    return render_template('mapTemp.html', grid=inpGrid, rect=inpRect, text=inpRectText,
                      circle=inpCircle, infoRect=inpInfoR, infoCircle=inpInfoC)


# set the routing for the filters
@app.route("/map/filter", methods = ["POST"])
def filterMap():

    area = request.form.get("AreaRange")
    depth = request.form.get("FindDepth")

    inpGrid = PYTHONSOURCES.createGrid()
    inpRect = PYTHONSOURCES.createRect(area)
    inpRectText = PYTHONSOURCES.createRectText()
    inpCircle = PYTHONSOURCES.createCircle(depth)
    inpInfoR = PYTHONSOURCES.infoBoxRect()
    inpInfoC = PYTHONSOURCES.infoBoxCircle()

    return render_template('mapTemp.html', grid=inpGrid, rect=inpRect, text=inpRectText,
                      circle=inpCircle, infoRect=inpInfoR, infoCircle=inpInfoC)


# set the routing for the main landing page
@app.route("/fields")
def printFields():
    inpFields = PYTHONSOURCES.fieldsHtml(None)
    return render_template('fieldsTemp.html', fields=inpFields)

@app.route("/fields/filter", methods = ["POST"])
def filterFields():
    field = request.form.getlist("field")
    inpFields = PYTHONSOURCES.fieldsHtml(field)
    return render_template('fieldsTemp.html', fields=inpFields)

# set the routing for the main landing page
@app.route("/finds")
def printFinds():
    inpFinds = PYTHONSOURCES.findsHtml(None)
    return render_template('findsTemp.html', finds=inpFinds)

@app.route("/finds/filter", methods = ["POST"])
def filterFinds():
    finds = request.form.getlist("find")
    inpFinds = PYTHONSOURCES.findsHtml(finds)
    return render_template('findsTemp.html', finds=inpFinds)


# set the routing for the main landing page
@app.route("/queries")
def printQueries():
    inpFinds = PYTHONSOURCES.findsQuery(None)
    inpFarmers = PYTHONSOURCES.farmerQuery(None)
    inpType = PYTHONSOURCES.typeQuery(None)

    return render_template('queriesTemp.html', queryFinds=inpFinds, queryFarmer=inpFarmers, queryType=inpType)

# set the routing for the filters
@app.route("/queries/filter", methods = ["POST"])
def filterQueries():
    find = request.form.get("finds")
    farm = request.form.get("farmer")
    type = request.form.get("type")

    inpFinds = PYTHONSOURCES.findsQuery(find)
    inpFarmers = PYTHONSOURCES.farmerQuery(farm)
    inpType = PYTHONSOURCES.typeQuery(type)

    return render_template('queriesTemp.html', queryFinds=inpFinds, queryFarmer=inpFarmers, queryType=inpType)

# call the main function
if __name__ == '__main__':
    app.run(debug=True)
