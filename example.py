from data_visualizer import Visualizer
from data_formation import import_dataframe


if  __name__ =='__main__':
      example1Data = import_dataframe("./Datasets/CrimeData_Test.csv")
      print("All datasets imported into memory.")
      runExample1 = Visualizer(example1Data)
      example2Data = import_dataframe("./Datasets/CrimeData_2018.csv")
      print("All datasets imported into memory.")
      runExample2 = Visualizer(example2Data)
      runExample1.plotCrimes()
      runExample2.plotCrimes()