# Nathan Bunch, Sumayyah Alahmadi, Jonathan Povish
# Project developed for the Dandyhacks Hackathon 2018
#
# This project is designed to analyze given crime data from
# the rochester police department. 
#

from data_formation import import_dataframe
from data_analyzer import getLat
from data_visualizer import doPlots
def getAllDfs():
    print("Grabbing data...")
    dfList = []
    print("0")
    crimeData2011 = import_dataframe("./Datasets/CrimeData_2011.csv")
    print("1")
    dfList.append(crimeData2011)
    crimeData2012 = import_dataframe("./Datasets/CrimeData_2012.csv")
    print("2")
    dfList.append(crimeData2012)
    crimeData2013 = import_dataframe("./Datasets/CrimeData_2013.csv")
    print("3")
    dfList.append(crimeData2013)
    crimeData2014 = import_dataframe("./Datasets/CrimeData_2014.csv")
    print("4")
    dfList.append(crimeData2014)
    crimeData2015 = import_dataframe("./Datasets/CrimeData_2015.csv")
    print("5")
    dfList.append(crimeData2015)
    crimeData2016 = import_dataframe("./Datasets/CrimeData_2016.csv")
    print("6")
    dfList.append(crimeData2016)
    crimeData2017 = import_dataframe("./Datasets/CrimeData_2017.csv")
    print("7")
    dfList.append(crimeData2017)
    crimeData2018 = import_dataframe("./Datasets/CrimeData_2018.csv")
    print("8")
    dfList.append(crimeData2018)
    test_data = import_dataframe("./Datasets/CrimeData_Test.csv")
    print("All datasets imported into memory.")
    return(dfList)
# in this file, the data should be prepared.

print(crimeData2011)


def addLad(df):
    locs = df['Geocode_Address'].tolist()
    Lats = []
    Longs = []
    for x in range(len(locs)):
        tempvar = getLat(locs[x])
        Lats.append(tempvar[0])
        Longs.append(tempvar[1])
    ser1 = pd.Series(Lats)
    ser2 = pd.Series(Longs)
    df = df.assign(Latitude = ser1, Longitude = ser2)
    return(df)
    
def writeToCsv(df,name):
    df.to_csv(name, sep=',', encoding='utf-8')


    
def MakeGraphsFromList(dfList):
    for x in range(len(dfList)):
       doPlots(dfList[x])
