import sys
sys.path.insert(0, './Quantum')
from kmeans_hybrid import QKMeans
from data_formation import import_dataframe_no_drop

df = import_dataframe_no_drop('./Datasets/CrimeData_Test_with_Lat_Lon.csv')
qkmeans = QKMeans(5)
# Latitude,Longitude
lats = df["Latitude"].tolist()
lons = df["Longitude"]
inputs = [[(lati/180),(loni/180)] for lati,loni in zip(lats, lons)]
#print(inputs)
qkmeans.train(inputs)
test_input = [[],[],[]]
qkmeans.classify()