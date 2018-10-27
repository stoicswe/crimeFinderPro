import sys
sys.path.insert(0, "./Quantum")
sys.path.insert(0, "./Classical")
sys.path.insert(0, "./Tensorflow")
import googlemaps
#import data_formation
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from kmeans_hybrid import QKMeans
import requests
import os
import pandas as pd
import geoplotlib
from tf_neural_network import TFNN

google_api_key = 'AIzaSyBSeHmttjDc95cXQ_psRD2zkDnU0XqzuO8'

def import_dataframe(csv_file = ''):
    #df = pd.DataFrame.from_csv(file)
    df = pd.read_csv(csv_file)
    print(df)
    labels_to_drop = ["Y", "OBJECTID", "Geocode_Street","Case_Number","Reported_Date_Year","Reported_Date_Month","Reported_Time","Reported_Timestamp","Address_StreetFull","Address_City","Address_State","Patrol_Beat","Patrol_Section","Case_Status","Statute_Title","Statute_Section","Statute_Subsection","Statute_Degree","Statute_Class","Statute_Text","Statute_Attempted","Geo_Beat","Geo_Section","Geo_Section_Num"]
    df = df.drop(labels=labels_to_drop, axis=1)
    return df

def getLatLon(address):
    gmaps = googlemaps.Client(key = key2)
    return(gmaps.geocode(address))

    
def getLat(x):   
    #address = "1600 Amphitheatre Parkway, Mountain View, CA"
    address = x
    api_key = google_api_key
    #address = "1600 Amphitheatre Parkway, Mountain View, CA"
    #api_key = "<api key copied from google>"
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        print(latitude)
        print(longitude)
        return([latitude,longitude])

# returns a complete quantum kmeans model
def qkmeans_analysis(X, y, k):
    inputs = [[xi,yi] for xi, yi in zip(X,y)]
    qkm = QKMeans(k)
    qkm.train(inputs)
    print("ClusterCentroids:")
    print(qkm.means)
    return qkm

def decision_tree_classification(X, y):
    dtc = DecisionTreeClassifier()
    dtc = dtc.fit(X,y)
    return dtc

def decision_tree_regression(X, y):
    dtr = DecisionTreeRegressor()
    dtr = dtr.fit(X,y)
    return dtr

def lineReg(X,y):
    regr = linear_model.LinearRegression()
    #Train the model using the training sets
    regr = regr.fit(X, y)
    return regr

def plotMaps(CrimeData): 
    crimeColumn = CrimeData['Geocode_Address'].tolist()
    data = []
    for x in range(len(crimeColumn)):
        tempvar = getLat(crimeColumn[x])
        data.append(tempvar)
        print(tempvar)
    geoplotlib.dot(data)
    geoplotlib.show()

#CrimeData = import_dataframe("C:/Users/jonp/Documents/School/Dandy/crimeFinderPro/Datasets/CrimeData_2018.csv")
#CrimeLoc = CrimeData[]