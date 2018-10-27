# Nathan Bunch
# 10/26/2018
# CrimeFinder Pro
# DandyHacks Hackathon Submission
# 
# This part of the program deals with formatting the data
# so that the analyzer can learn upon the data to make predictions
# and to give the data a user-friendly view of the data for manual analysis.

import pandas as np
import numpy as py
import random
import csv

def import_data(file):
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lines = 0
        for row in csv_reader:
            print(f'Columns: {", ".join(row)}')
            lines += 1
        print(row["Geocode Address"])
