# Nathan Bunch
# 10/26/2018
# CrimeFinder Pro
# DandyHacks Hackathon Submission
# 
# This part of the program deals with formatting the data
# so that the analyzer can learn upon the data to make predictions
# and to give the data a user-friendly view of the data for manual analysis.

import pandas as pd
import numpy as py
import random
import csv

def import_data(file):
    """with open(file, mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        lines = 0
        print(csv_reader)
        for row in csv_reader:
            if lines == 0:
                print(f'Columns: {", ".join(row)}')
                lines += 1
            print(f'\t{row["GeocodeAddress"]}')
            lines += 1"""
    df = pd.DataFrame.from_csv(file)
    print(df)
    

import_data("CrimeData.csv")
