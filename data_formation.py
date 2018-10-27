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

#def import_row(file, columnLabel):
#    with open(file, mode='r', encoding="utf-8") as csv_file:
#        csv_reader = csv.DictReader(csv_file)
#        lines = 0
        #for row in csv_reader:
        #    if lines == 0:
        #        print(f'Columns: {", ".join(row)}')
        #        lines += 1
        #    print(f'\t{row["GeocodeAddress"]}')
        #    lines += 1
#        returnData = []
#        lines = 0
#        for row in csv_reader:
#            if lines == 0:
#                print("Grabing Data")
#                lines += 1
#            returnData.append(row[columnLabel])
#        return returnData
            

def import_dataframe(file):
    #df = pd.DataFrame.from_csv(file)
    df = pd.read_csv(file)
    print(df)
    labels_to_drop = ["Y", "OBJECTID", "Geocode_Street","Case_Number","Reported_Date_Year","Reported_Date_Month","Reported_Time","Reported_Timestamp","Address_StreetFull","Address_City","Address_State","Patrol_Beat","Patrol_Section","Case_Status","Statute_Title","Statute_Section","Statute_Subsection","Statute_Degree","Statute_Class","Statute_Text","Statute_Attempted","Geo_Beat","Geo_Section","Geo_Section_Num"]
    df = df.drop(labels=labels_to_drop, axis=1)
    return df

#print(import_dataframe("./Datasets/CrimeData_2011.csv"))