# Nathan Bunch, Jonathan Povish
# Project developed for the 
#
#
#

from data_formation import import_dataframe

print("Grabbing data...")
print("0")
crimeData2011 = import_dataframe("./Datasets/CrimeData_2011.csv")
print("1")
crimeData2012 = import_dataframe("./Datasets/CrimeData_2012.csv")
print("2")
crimeData2013 = import_dataframe("./Datasets/CrimeData_2013.csv")
print("3")
crimeData2014 = import_dataframe("./Datasets/CrimeData_2014.csv")
print("4")
crimeData2015 = import_dataframe("./Datasets/CrimeData_2015.csv")
print("5")
crimeData2016 = import_dataframe("./Datasets/CrimeData_2016.csv")
print("6")
crimeData2017 = import_dataframe("./Datasets/CrimeData_2017.csv")
print("7")
crimeData2018 = import_dataframe("./Datasets/CrimeData_2018.csv")
print("8")
test_data = import_dataframe("./Datasets/CrimeData_Test.csv")
print("All datasets imported into memory.")

# in this file, the data should be prepared.

print(crimeData2011)

