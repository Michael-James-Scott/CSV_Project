import matplotlib.pyplot as plt 
import csv
from datetime import datetime
open_file = open("sitka_weather_07-2018_simple.csv", "r")
csv_file = csv.reader(open_file,delimiter=",")
header_row = next(csv_file)

#plt.plot([1,2,3,4,5],color="red")

#plt.show()

for index, column_header in enumerate(header_row):
    print(index,column_header)

highs= []
dates = []
lows = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    dates.append(row[2])

print(highs[:10])    
fig = plt.figure()
plt.plot(dates, highs, color="red", alpha = 0.5)
plt.plot(dates, lows,color="blue", alpha = 0.5)
current_date=datetime.strptime(row[2], '%Y-%m-%d')
plt.fill_between(dates,highs,lows,facecolor="purple", alpha = 0.25)
plt.title("daily high temps, July 2018", fontsize = 12)
plt.xlabel("Dates",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis='both', which = "major", labelsize=12)
fig.autofmt_xdate()

plt.show()
   # if rows
    #    highs.append(rows)
    
