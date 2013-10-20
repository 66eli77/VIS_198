# Eli Dai a11062387
# VIS 198  assignment 1
import json
fname = "/Users/elidai/Desktop/sdsc.json"
infile = open(fname,'r')
data = infile.read()
mydata = json.loads(data)

# Part 1: Individual Keys -------------------------------------------------------------------------------
print("Part 1: ")
# writes over the last minute

for i in range(20):
	length_min = len(mydata[i]["datapoints"])
	# adding a filter to avoid 'null' in the list
	total_min = sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_min - 6):length_min])[0])))
	avg_min = float(total_min / 6)
	print("P1 writes over the last minute: " + str(avg_min))
	
# writes over the last hour

for i in range(20):
	length_hr = len(mydata[i]["datapoints"])
	# adding a filter to avoid 'null' in the list
	total_hr = sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_hr - 360):length_hr])[0])))
	avg_hr = float(total_hr / 360)
	print("P1 writes over the last hour: " + str(avg_hr))
	
# writes over the last day

for i in range(20):
	length_day = len(mydata[i]["datapoints"])
	# adding a filter to avoid 'null' in the list
	total_day = sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_day - 8640):length_day])[0])))
	avg_day = float(total_day / 8640)
	print("P1 writes over the last day: " + str(avg_day))
	
# Part 2: Same Key, All Hosts ---------------------------------------------------------------------------
print("Part 2: ")
a = [0,5,10,15]
b = [1,6,11,16]
c = [2,7,12,17]
d = [3,8,13,18]
e = [4,9,14,19]
outloop = [a,b,c,d,e]

# writes over the last minute

for j in outloop:
	total_min_P2 = 0
	for i in j:
		length_min_P2 = len(mydata[i]["datapoints"])
		total_min_P2 += sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_min_P2 - 6):length_min_P2])[0])))
	avg_min_P2 = float(total_min_P2 / 24)
	print("P2 writes over the last minute: " + str(avg_min_P2))
	
# writes over the last hour

for j in outloop:
	total_hr_P2 = 0
	for i in j:
		length_hr_P2 = len(mydata[i]["datapoints"])
		total_hr_P2 += sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_hr_P2 - 360):length_hr_P2])[0])))
	avg_hr_P2 = float(total_hr_P2 / 1440)
	print("P2 writes over the last hour: " + str(avg_hr_P2))

# writes over the last day

for j in outloop:
	total_day_P2 = 0
	for i in j:
		length_day_P2 = len(mydata[i]["datapoints"])
		total_day_P2 += sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_day_P2 - 8640):length_day_P2])[0])))
	avg_day_P2 = float(total_day_P2 / 34560)
	print("P2 writes over the last day: " + str(avg_day_P2))
	
# Part 3: All Keys, All Hosts ----------------------------------------------------------------------------------
print("Part 3: ")
# writes over the last minute

total_min_P3 = 0
for i in range(20):
	length_min_P3 = len(mydata[i]["datapoints"])
	total_min_P3 += sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_min_P3 - 6):length_min_P3])[0])))
avg_min_P3 = float(total_min_P3 / 120)
print("P3 writes over the last minute: " + str(avg_min_P3))

# writes over the last hour

total_hr_P3 = 0
for i in range(20):
	length_hr_P3 = len(mydata[i]["datapoints"])
	total_hr_P3 += sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_hr_P3 - 360):length_hr_P3])[0])))
avg_hr_P3 = float(total_hr_P3 / 7200)
print("P3 writes over the last hour: " + str(avg_hr_P3))

# writes over the last day

total_day_P3 = 0
for i in range(20):
	length_day_P3 = len(mydata[i]["datapoints"])
	total_day_P3 += sum(filter(None, list(zip(*mydata[i]["datapoints"][(length_day_P3 - 8640):length_day_P3])[0])))
avg_day_P3 = float(total_day_P3 / 172800)
print("P3 writes over the last day: " + str(avg_day_P3))
