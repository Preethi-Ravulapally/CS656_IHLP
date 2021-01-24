
"""
Created on Tue Mar 24 16:46:11 2020
For CS526 Chicago Crime Data Visualisation
"""
import pandas as pd
import numpy as np
import json
import datetime
import os
file_name=""        # for storing the filename
from flask import Flask, render_template, jsonify, request, flash, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename


app = Flask(__name__)
use_cols=['Date','Domestic','PrimaryType','District','Arrest','Year','FBICode','LocationDescription']

# reading data from file
data = pd.read_csv('C:\\Users\\TRANS20-LAP-RA1\\Downloads\\Data.csv', usecols=use_cols, iterator=True, chunksize=100000)
data = pd.concat(data, ignore_index=True)
dist_dict={1:"Central", 2:"Wentworth", 3:"Grand Crossing", 4:"South Chicago", 5:"Calumet", 6:"Gresham",
            7:"Eaglewood", 8:"Chicago Lawn", 9:"Deering", 10:"Ogden", 11:"Harrison", 12:"Near West",
           14:"Shakespeare", 15:"Austin", 16:"Jefferson Park", 17:"Albany Park", 18:"Near North",
           19:"Town Hall", 20:"Lincoln", 22:"Morgan Park", 24:"Rogers Park", 25:"Grand Central"}  #district names
rm_dist = {1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,24,25} # district numbers
data = data[data.District.isin(rm_dist)]

#-----------------------------------------------
#   methods for data processing and visualisation
#-----------------------------------------------

def myconverter(obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj,datetime.datetime):
            return obj.__str__()

# Visualisation for pie chart
# ---------------------------------------------------------
# function  pie_chart
# inputs: Dataframe
# Output: dictionary with data converted to json format
#-----------------------------------------------------------

# ---------------------------------------------------------
# function main_page
# inputs: None
# Output: Render template
#-----------------------------------------------------------
@app.route('/')
def main_page():
    return render_template('main.html')



# Run the main application and start the instance
if __name__ == "__main__":
    app.debug = True
    app.run()

