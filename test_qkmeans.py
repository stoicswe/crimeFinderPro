import sys
sys.path.insert(0, './Quantum')
from kmeans_hybrid import QKMeans
from data_formation import import_dataframe_no_drop

df = import_dataframe_no_drop('./Datasets/CrimeData_Test_with_Lat_Lon.csv')
test_df = import_dataframe_no_drop('./Datasets/Test_Lat_Lon.csv')
qkmeans = QKMeans(5)
# Latitude,Longitude
lats = df["Latitude"].tolist()
lons = df["Longitude"].tolist()
# inputs = [[(lati/180),(loni/180)] for lati,loni in zip(lats, lons)]
inputs = [[(lati),(loni)] for lati,loni in zip(lats, lons)]
#print(inputs)
qkmeans.train(inputs)
lats = test_df["Latitude"].tolist()
lons = test_df["Longitude"].tolist()
# test_inputs = [[(lati/180),(loni/180)] for lati,loni in zip(lats, lons)]
test_inputs = [[(lati),(loni)] for lati,loni in zip(lats, lons)]
print(qkmeans.means)
classifications = []
for crd in test_inputs:
    classifications.append(qkmeans.classify(crd))
print(classifications)