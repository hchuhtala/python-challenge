# Import the aperating system module
import os
# Module for reading CSV files
import csv

#Initalize lists and variables
date = []
money = []
total = 0
change = []

csvpath = os.path.join('..', 'Resources', 'budget_data.csv') 
# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header to lists
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
  
    # The total number of months 
    month_count=len(date)

    # The net total amount of "Profit/Losses" over the entire period
    #print("Total Value: $"+ str(sum(money)))

    # The average of the changes in "Profit/Losses" over the entire period
    change = [j - i for i, j in zip(money[: -1], money[1 :])]
    avg = sum(change) / (month_count - 1)
    #print(len(change))
    change.insert(0,0) #add a 0 in the first position to make list the same length as date
    #print(len(change))
   
    # The greatest increase in profits (date and amount) over the entire period
    full_dict = dict(zip(date, change))
    max_key, max_value = max(full_dict.items(), key = lambda p: p[1])
 
    # The greatest decrease in losses (date and amount) over the entire period
    min_key, min_value = min(full_dict.items(), key = lambda p: p[1])
    
    # Print Report
    print("Financal Analysis:")
    print("--------------------")
    print("Total Months: " + str(month_count))
    print("Total Value: $"+ str(sum(money)))
    print("Average Change: $" + str(round(avg))) 
    print("Greatest Increase: " + str(max_key) + " $" + str(max_value))
    print("Greatest Decrease: " + str(min_key) + " $" + str(min_value))

# Specify the file to write to
output_path = os.path.join("financal_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
txtfile = open(output_path, 'w')

# Write the first row (column headers)
txtfile.write("Financal Analysis:\n")

# Write the rest of the rows
txtfile.write("Total Months: " + "$" + str(month_count) + "\n")
txtfile.write("Total Value: " + "$" + str(sum(money)) + "\n")
txtfile.write("Average Change: " + "$" + str(round(avg)) + "\n")
txtfile.write("Greatest Increase: " + str(max_key) + " $" + str(max_value) + "\n")
txtfile.write("Greatest Decrease: " + str(min_key) + " $" + str(min_value) + "\n")
txtfile.close()