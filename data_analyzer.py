import sys
sys.path.insert(0, "./Quantum")
sys.path.insert(0, "./Classical")
sys.path.insert(0, "./Tensorflow")
import googlemaps
import sklearn
from sklearn import linear_model
from kmeans_hybrid import QKMeans

gmaps = googlemaps.Client(key='AIzaSyDlPGwvHDrnUh7cugYNIngmJPmZAWAN_VY')

# returns a complete quantum kmeans model
def qkmeans_analysis(X, y, k):
    inputs = [[xi,yi] for xi, yi in zip(X,y)]
    qkm = QKMeans(k)
    qkm.train(inputs)
    print("ClusterCentroids:")
    print(qkm.means)
    return qkm
<<<<<<< HEAD
=======

def decision_tree_classification(X, y):
    dtc = sklearn.tree.DecisionTreeClassifier()
    dtc = dtc.fit(X,y)
    return dtc

def decision_tree_regression(X, y):
    dtr = sklearn.tree.DecisionTreeRegressor()
    dtr = dtr.fit(X,y)
    return dtr

def lineReg(X,y):
    regr = linear_model.LinearRegression()
 # Train the model using the training sets
    regr.fit(X_train, Y_train)
    return(regr)

>>>>>>> 8c5bb0b4c0378686de23cb0a107b41aca45de1c2
