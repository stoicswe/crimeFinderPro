import sys
sys.path.insert(0, "./Quantum")
sys.path.insert(0, "./Classical")
sys.path.insert(0, "./Tensorflow")
import googlemaps
import sklearn
import geoplotlib
from kmeans_hybrid import QKMeans

# returns a complete quantum kmeans model
def qkmeans_analysis(X, y, k):
    inputs = [[xi,yi] for xi, yi in zip(X,y)]
    qkm = QKMeans(k)
    qkm.train(inputs)
    print("ClusterCentroids:")
    print(qkm.means)
    return qkm

