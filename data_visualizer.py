import matplotlib.pyplot as plt
import random
import numpy as np
from datetime import datetime
import data_formation
''' Below is an example of a simple pie chart 
labels = 'Python', 'C++', 'Ruby', 'Java'
#Replace this with labels of crime
sizes = [215, 130, 245, 210]
#Replace this with # of people per crime
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice


plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()
'''


#Replace Vals With #of crime
def plotCrimes():
    #Working Currently Right here
    crimeColumn = CrimeData['StatuteCrimeCategory'].tolist()
    #Below line change the 'time' to time crime it is'
    sexColumn = CrimeData['StatuteCategory'].tolist()    
    crimes = list(set(crimeColumn))
    vals = []
    for x in range(len(crimes)):
        vals.append([0,0])
    for y in range(len(crimeColumn)):
        if(sexColumn[y] == 'M'):
            vals[crimes.index(crimeColumn[y])][0] += 1
        else:
            vals[crimes.index(crimeColumn[y])][1] += 1
        
    vals = np.asarray(vals)
    #vals = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
    fig, ax = plt.subplots()
    print(vals)
    ax.pie(vals.flatten(), radius=1.2, colors=plt.rcParams["axes.prop_cycle"].by_key()["color"][:vals.shape[1]])
    ax.pie(vals.sum(axis=1), radius=1)
    ax.set(aspect="equal", title='Pie plot with `ax.pie`')
    plt.show()
    #clf()
    #close()


def plotHours():
    #Below line change the 'crime' to whatever crime it is'
    crimeColumn = CrimeData['StatuteCrimeCategory'].tolist()
    #Below line change the 'time' to time crime it is'
    dateColumn = CrimeData['Time'].toList()

    crimesType = list(set(crimeColumn))
    CrimeTimeSplit = []

    for type in range(len(crimesType)):
        CrimeTimeSplit.append([])

    for z in range(len(crimes)):
        CrimeTimeSplit[crimesType.index(crimes[x])].append(int(dateColumn[z]/100))
    #import matplotlib.pyplot as plt
    xAxis = [range(23)]
    for x in range(len(xAxis)):
        yAxis.append(xAxis.count(xAxis[x]))
    # make up some data
    #x = [datetime.datetime.now() + datetime.timedelta(hours=i) for i in range(12)]
    #y = [i+random.gauss(0,1) for i,_ in enumerate(x)]
    # plot
    lines = plt.plot(xAxis,yAxis)
    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    plt.show()


def plotDays():
    #Below line change the 'crime' to whatever crime it is'
    crimeColumn = CrimeData['Statute_Category'].toList()
    #Below line change the 'time' to where the full time crime it is'
    dateColumn = CrimeData['Time'].toList()
    
    crimesType = list(set(crimeColumn))
    CrimeDaySplit = []
    totalTime = []
    
    for type in range(len(crimesType)):
        CrimeDaySplit.append([])

    for z in range(len(crimes)):
        d = datetime.strptime(dateColumn[z].split(",")[0], "%m/%d/%Y")

        totalTime.append(d.weekday())
        CrimeTimeSplit[crimesType.index(crimes[x])].append(d.weekday())
        
    objects = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    performance = []
    for x in range(len(object)):
        performance.append(totalTime.count(x))
    #performance = [10,8,6,4,2,1]
    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Usage')
    plt.title('Programming language usage')
    plt.show()

CrimeData = data_formation.import_dataframe("CrimeData.csv")