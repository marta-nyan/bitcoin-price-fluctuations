#BITCOIN VALUE ANALYSIS
#This program carries out calculations/builds plots to describe and analyse bitcoin value in the period 2010-2018
#This program carries out 5 tasks
#(0) imports the data
#(1) finds the highest and lowest ever values of Bitcoin and when they occurred
#(2) creates a plot showing the value of Bitcoin since 2010
#(3) creates a plot showing both the daily value of Bitcoin at the end of each day and the weekly average value in 2018
#(4) Gives the days when it was best and worst to invest £100 if the investor was to resell after 14 days     
#    


#TASK 0
##################################################################################################################################################
import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import datetime
data = []
with open("bitcoin.json") as f:
    for i,j in json.load(f)["bpi"].items():
        data.append([datetime.strptime(i, "%Y-%m-%d"), j])

  
#TASK 1
##################################################################################################################################################

#create lists of all the values and dates
        
values = []
dates = []
for date, value in data:
    values.append(value)
    dates.append(date)
    
# max(values) finds the highest value
# to find the date when the value occurres,
# we find the index of max(values) and extract the date with date[index]
for i , value in enumerate (values,0):
      if value == max(values):
        max_date = dates[i]
print ('Highest value of Bitcoin (from 7/2010 to 1/2019):', max(values))
print ('Date registered:', max_date)

# min(values) finds the lowest value
# to find the date when the value occurres,
# we find the index of max(values) and extract the date with date[index]
for i , value in enumerate (values,0):
      if value == min(values):
        min_date = dates[i]
print ('Lowest value (from 7/2010 to 1/2019):', min(values))
print ('Date registered:', min_date)
        
#TASK 2
##################################################################################################################################################

#plot the value of bitcoin 2010-2018
plt.plot(dates,values, color='#696969')
plt.grid()
#add maximum and minimum
plt.plot(min_date,min(values),'o',color='black')
plt.plot(max_date,max(values),'o',color='black')
plt.ylabel ("Price(in £)")
plt.title (" Price (GBP) of Bitcoin from July 2010 to November 2019")

plt.show()
from matplotlib import pyplot as mp
mp.savefig('2010-2019 prices.png')

#TASK 3
##################################################################################################################################################

# extract the date and values for 2018 only
yearly_dates = dates[-383:-18]
yearly_values = values[-383:-18]

# to find the weekly bitcoin value,
# - split list into 52 lists of 7 elements  
split_list_weekly = [yearly_values[i:i+7] for i in range(0,len(dates[-383:-18])-7,7)]
# - create a list containing the mean of the 7 elements in each of of the 52 lists
weekly_value = [np.mean(split_list_weekly[i]) for i in range(0,len(split_list_weekly))]

# to find the x-coordinate of each weekly value,
# extract the forth day from each week (so that we plot in the middle of the week)
# however, we want the plots to start together, so we choose to plot
# the first week average on the first day for the first week 
# and the last week average on the last day of the last week 
weeks = [yearly_dates[0]]+[yearly_dates[i+7] for i in range(4,len(dates[-383:-18])-11,7)]+[yearly_dates[-1]]


plt.plot (yearly_dates,yearly_values, color = 'green')
plt.plot (weeks,weekly_value, color ="red")
plt.grid()
plt.ylabel ("Price of Bitcoin (in £)")
plt.title (" Price (GBP) of Bitcoin in 2018")
# add a legend
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
red_patch = mpatches.Patch(color='red', label='average weekly value')
green_patch = mpatches.Patch(color='green', label='daily value')
plt.legend(handles=[red_patch,green_patch])

plt.show()


#TASKS 4
##################################################################################################################################################



# create a list values_order = [1st value, 14th value, 2nd value, 15th value, 3rd value, 16th value etc ]
values_order = []
i = 0
for i in range(0, len(values)-14):
      values_order.append(values[i])
      values_order.append(values[i+14])
# create a list of lists = [[1st value, 14th value],[[2nd value, 15th value]], [[3rd value, 16th value]], etc ], call this list list_values_order
list_values_order = [values_order[i:i+2] for i in range(0,len(values_order),2)]
# for each of this lists calculate the percentage increase (because this determines the biggest gain or loss from investing £100)
percentage_increase = [(np.diff(list_values_order[i])/(list_values_order[i][0]) * 100) for i in range(0,len(list_values_order))]


# create a list such that [1st day, 14th day, 2nd day, 15th day, 3rd day, 16th day etc ]
dates_order = []
i = 0
for i in range(0, len(dates)-14):
      dates_order.append(dates[i])
      dates_order.append(dates[i+14])
# create a list of lists = [[1st day, 14th day],[[2nd day, 15th day]], [[3rd day, 16th day]], etc ], we call this list_dates_order    
list_dates_order = [dates_order[i:i+2] for i in range(0,len(dates_order),2)]

#we are gonna use this to trace back to the date from the percentage increase, as the two corresponding values will have the same index
#find max percentage increase and day it occurred
for i , value in enumerate (percentage_increase,0):
      if value == max(percentage_increase):
        max_profit_day = list_dates_order[i][0] #we add [0] because we want the first element of a list of two

print ('Highest profit:  £', max(percentage_increase)[0])
print ('Date registered:', max_profit_day)

#find the max percentage decrease and day ot occurred
for i , value in enumerate (percentage_increase,0):
      if value == min(percentage_increase):
        min_profit_day = list_dates_order[i][0]

print ('Most significant loss: £', -(min(percentage_increase))[0])
print ('Date registered:', min_profit_day)
