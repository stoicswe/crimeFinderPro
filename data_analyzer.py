import sys
sys.path.insert(0, "./Quantum")
sys.path.insert(0, "./Classical")
sys.path.insert(0, "./Tensorflow")
from geoplotlib.colors import create_set_cmap
import pyglet
from sklearn.cluster import KMeans
import geoplotlib
from geoplotlib.layers import BaseLayer
from geoplotlib.core import BatchPainter
from geoplotlib.utils import BoundingBox
import numpy as np
import googlemaps
#import data_formation
#from sklearn import linear_model
#from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from kmeans_hybrid import QKMeans
import requests
import os
import pandas as pd
import geoplotlib
from tf_neural_network import TFNN

google_api_key = 'AIzaSyBSeHmttjDc95cXQ_psRD2zkDnU0XqzuO8'

class KMeansLayer(BaseLayer):

    def __init__(self, data):
        self.data = data
        self.k = 2


    def invalidate(self, proj):
        self.painter = BatchPainter()
        x, y = proj.lonlat_to_screen(self.data['Longitude'], self.data['Latitude'])

        k_means = KMeans(n_clusters=self.k)
        k_means.fit(np.vstack([x,y]).T)
        labels = k_means.labels_

        self.cmap = create_set_cmap(set(labels), 'hsv')
        for l in set(labels):
            self.painter.set_color(self.cmap[l])
            self.painter.convexhull(x[labels == l], y[labels == l])
            self.painter.points(x[labels == l], y[labels == l], 2)
    
            
    def draw(self, proj, mouse_x, mouse_y, ui_manager):
        ui_manager.info('Use left and right to increase/decrease the number of clusters. k = %d' % self.k)
        self.painter.batch_draw()


    def on_key_release(self, key, modifiers):
        if key == pyglet.window.key.LEFT:
            self.k = max(2,self.k - 1)
            return True
        elif key == pyglet.window.key.RIGHT:
            self.k = self.k + 1
            return True
        return False
  




def import_dataframe(csv_file = ''):
    #df = pd.DataFrame.from_csv(file)
    df = (csv_file)
    print(df)
    labels_to_drop = ["Y", "OBJECTID", "Geocode_Street","Case_Number","Reported_Date_Year","Reported_Date_Month","Reported_Time","Reported_Timestamp","Address_StreetFull","Address_City","Address_State","Patrol_Beat","Patrol_Section","Case_Status","Statute_Title","Statute_Section","Statute_Subsection","Statute_Degree","Statute_Class","Statute_Text","Statute_Attempted","Geo_Beat","Geo_Section","Geo_Section_Num"]
    df = df.drop(labels=labels_to_drop, axis=1)
    return df

def getLatLon(address):
    gmaps = googlemaps.Client(key = key2)
    return(gmaps.geocode(address))

    
def getLat(x):   
    google_api_key = 'AIzaSyBSeHmttjDc95cXQ_psRD2zkDnU0XqzuO8'

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
    #Assuming DF has lat/long
    '''
    crimeColumn = CrimeData['Geocode_Address'].tolist()
    LatColumn = CrimeData['Latitude'].tolist()
    LongColumn = CrimeData['Longitude'].tolist()
    data = []
    '''
    
    vals = list(CrimeData.columns.values)
    vals.remove("Latitude")
    vals.remove("Longitude")
    Data = CrimeData.drop(vals, axis = 1)
    #for x in range(len(LatColumn)):
     #   data.append([LatColumn[x],LongColumn[x]])
    #print(vals)
    Data.to_csv("TempFileName2.csv", sep=',', encoding='utf-8')
    data = geoplotlib.utils.read_csv('TempFileName2.csv') 
    geoplotlib.add_layer(KMeansLayer(data)) 
    geoplotlib.set_smoothing(True) 
    geoplotlib.set_bbox(geoplotlib.utils.BoundingBox.DK) 
    geoplotlib.show() 

    
    
    #geoplotlib.dot(data)
    #geoplotlib.show()



test_data = pd.read_csv("./Datasets/CrimeData_Test_with_Lat_Lon.csv")
plotMaps(test_data)
#CrimeData = import_dataframe("C:/Users/jonp/Documents/School/Dandy/crimeFinderPro/Datasets/CrimeData_2018.csv")
#CrimeLoc = CrimeData[]
