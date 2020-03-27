# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Reading using CSV module

date = []
money = []
total = 0
change = []
total_delta = 0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header to lists
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        total = int(total) + int(row[1]) #calc total profits and losses
        #delta = int(row[1]) - next(iter(row[1]))
        #change.append(delta)
    #for i in money:
       # print(i)
    
        #delta = (i+1) - (i)
        #print(delta)
        #total_delta= total_delta + delta
        #change.append(delta)  

    # The total number of months 
    month_count=len(money)
    print("Financal Analysis:")
    print("--------------------")
    print("Total Months: " + str(month_count))

    # The net total amount of "Profit/Losses" over the entire period
    print("Total Value: $"+ str(total))
    #print("Total Value: $"+ str(sum(money)) why doesn't this work??

    # The average of the changes in "Profit/Losses" over the entire period
    change = [j - i for i, j in zip(money[: -1], money[1 :])] #can you explain this??
    avg = sum(change) / month_count #why isn't avg a float?
    #avg = total_delta / month_count
    print("Average Change: $" + str(avg))
    #print("Average Change: $" + str(round(avg)) Why doesn't this work??

    # The greatest increase in profits (date and amount) over the entire period
    max_delta = max(change)
    for x in change
        if change == max_delta:
            return(x)
    
    print("Greatest Increase: $" + date[x] + str(max_delta))

    # The greatest decrease in losses (date and amount) over the entire period
    min_delta = min(change)
    print("Greatest Decrease: $" + str(min_delta))