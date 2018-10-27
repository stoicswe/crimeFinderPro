import matplotlib.pyplot as plt
import random
from datetime import datetime

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
def plotCrimes()
    vals = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
    fig, ax = plt.subplots()
    ax.pie(vals.flatten(), radius=1.2,
           colors=plt.rcParams["axes.prop_cycle"].by_key()["color"][:vals.shape[1]])
    ax.pie(vals.sum(axis=1), radius=1)
    ax.set(aspect="equal", title='Pie plot with `ax.pie`')
    plt.show()
    clf()
    close()


def plotHours():
    #Below line change the 'crime' to whatever crime it is'
    crimeColumn = CrimeData['Crime'].toList()
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
    crimeColumn = CrimeData['Crime'].toList()
    #Below line change the 'time' to where the full time crime it is'
    dateColumn = CrimeData['Time'].toList()
    
    crimesType = list(set(crimeColumn))
    CrimeDaySplit = []
    totalTime = []
    
    for type in range(len(crimesType)):
        CrimeDaySplit.append([])

    for z in range(len(crimes)):
        d = datetime.strptime(dateColumn[z].split(",")[0], "%m/%d/%Y")

        totalTime.append(d.weeday())
        CrimeTimeSplit[crimesType.index(crimes[x])].append(d.weekday())
        


