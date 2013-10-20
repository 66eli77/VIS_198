import numpy as np
import matplotlib.pyplot as plt

import json
fname = "/Users/elidai/Desktop/sdsc.json"
infile = open(fname,'r')
data = infile.read()
mydata = json.loads(data)
a = []
b = []
c = []

for i in range(20):
	length_day = len(mydata[i]["datapoints"])
	# adding a filter to avoid 'null' in the list.
	total_day = sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_day - 8640):length_day])[0])))
	avg_day = float(total_day / 8640)
	a.append(avg_day)

for i in range(20):
	length_hr = len(mydata[i]["datapoints"])
	# adding a filter to avoid 'null' in the list
	total_hr = sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_hr - 360):length_hr])[0])))
	avg_hr = float(total_hr / 360)
	b.append(avg_hr)
	
for i in range(20):
	length_day = len(mydata[i]["datapoints"])
	# adding a filter to avoid 'null' in the list
	total_day = sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_day - 8640):length_day])[0])))
	avg_day = float(total_day / 8640)	
	c.append(avg_day)
		
x = np.arange(20)
y = np.asarray(a)
area1 = np.pi * np.asarray(a) **0.1

q = np.arange(20)
p = np.asarray(b)
area2 = np.pi * np.asarray(b) **0.3

m = np.arange(20)
n = np.asarray(c)
area3 = np.pi * np.asarray(c) **0.6

plt.scatter(x, y, s=area1, alpha=0.4, color = 'red')  # minut
plt.scatter(q, p, s=area2, alpha=0.4, color = 'blue')  # hour
plt.scatter(m, n, s=area3, alpha=0.4, color = 'yellow')  # day

plt.show()