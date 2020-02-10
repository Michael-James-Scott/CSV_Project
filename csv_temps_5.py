import matplotlib.pyplot as plt 
import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(open_file,delimiter=",")
header_row = next(csv_file)

open_file2 = open("death_valley_2018_simple.csv", "r")
csv_file2 = csv.reader(open_file2,delimiter=",")
header_row2 = next(csv_file2)


for index, column_header in enumerate(header_row):
    print(index,column_header)

highs= []
dates = []
lows = []

for row in csv_file:
    try:
        high = int(row[5])
        low = int(row[6])
        current_date=datetime.strptime(row[2], '%Y-%m-%d')
        title = str(row[1])
    except ValueError:
        print(f"Missing data for {current_date}")
    else: 
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


highs2= []
dates2 = []
lows2 = []

for row in csv_file2:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date=datetime.strptime(row[2], '%Y-%m-%d')
        title2 = str(row[1])
    except ValueError:
        print(f"Missing data for {current_date}")
    else: 
        highs2.append(high)
        lows2.append(low)
        dates2.append(current_date)
 
fig, axs = plt.subplots(2)
fig.suptitle('Temperature Comparison Between ' + title + ' and '+ title2)
axs[0].plot(dates, highs, color="red", alpha = 0.5)
axs[0].plot(dates, lows,color="blue", alpha = 0.5)
current_date=datetime.strptime(row[2], '%Y-%m-%d')
axs[0].fill_between(dates,highs,lows,facecolor="purple", alpha = 0.25)
axs[0].set_title(title, fontsize = 12)
#axs[0].xlabel("Dates",fontsize=12)
#axs[0].ylabel("Temperature (F)",fontsize=12)
axs[0].tick_params(axis='both', which = "major",  labelsize=12)
fig.autofmt_xdate()


axs[1].plot(dates2, highs2, color="red", alpha = 0.5)
axs[1].plot(dates2, lows2,color="blue", alpha = 0.5)
current_date=datetime.strptime(row[2], '%Y-%m-%d')
axs[1].fill_between(dates2,highs2,lows2,facecolor="purple", alpha = 0.25)
axs[1].set_title(title2, fontsize = 12)
#axs[1].xlabel("Dates",fontsize=12)
#axs[1].ylabel("Temperature (F)",fontsize=12)
axs[1].tick_params(axis='both', which = "major", labelsize=12)
fig.autofmt_xdate()

plt.show()
