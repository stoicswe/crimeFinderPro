from data_visualizer import doPlots
from data_formation import import_dataframe

def runExample(df):
    doPlots(df)

if  __name__ =='__main__':
      testData = import_dataframe("./Datasets/CrimeData_Test.csv")
      print("All datasets imported into memory.")
      runExample(testData)