import sys
sys.path.insert(0, "./Quantum")
sys.path.insert(0, "./Classical")
sys.path.insert(0, "./Tensorflow")
import googlemaps
import data_formation
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from kmeans_hybrid import QKMeans
import requests
import os


def getLatLon(address):
    return gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    
def getLat(x):   
    #address = "1600 Amphitheatre Parkway, Mountain View, CA"
    address = x
    api_key = "AIzaSyDlPGwvHDrnUh7cugYNIngmJPmZAWAN_VY"
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        print ('Latitude:' + str(latitude))
        print ('Longitude:' + str(longitude))
    return(list(str(latitude),str(longitude)))

# returns a complete quantum kmeans model
def qkmeans_analysis(X, y, k):
    inputs = [[xi,yi] for xi, yi in zip(X,y)]
    qkm = QKMeans(k)
    qkm.train(inputs)
    print("ClusterCentroids:")
    print(qkm.means)
    return qkm

def decision_tree_classification(X, y):
    dtc = sklearn.tree.DecisionTreeClassifier()
    dtc = dtc.fit(X,y)
    return dtc

def decision_tree_regression(X, y):
    dtr = sklearn.tree.DecisionTreeRegressor()
    dtr = dtr.fit(X,y)
    return dtr

def lineReg(X,y):
    regr = sklearn.linear_model.LinearRegression()
    #Train the model using the training sets
    regr.fit(X_train, Y_train)
    return(regr)

def plotMaps(): 
    crimeColumn = CrimeData['Geocode_Address'].tolist()
    data = []
    for x in range(len(crimeColumn)):
        data.append(getLat(crimeColumn[x]))
    
    
    geoplotlib.dot(data)
    geoplotlib.show()

CrimeData = data_formation.import_dataframe("C:/Users/jonp/Documents/School/Dandy/crimeFinderPro/Datasets/CrimeData_2012.csv")
#CrimeLoc = CrimeData[]
    
    
