
# Import the operating system module
import os
# Module for reading CSV files
import csv

#Initalize lists and variables
date = []
money = []
total = 0
change = []
diff = []
total_delta = 0

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    csv_first_row = next(csvreader)
    date.append(csv_first_row[0])
    money.append(int(csv_first_row[1]))
    prev = csv_first_row[1]
    #print(prev)
    # Read each row of data after the header to lists
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        total = int(total) + int(row[1]) #calc total profits and losses
        #save prev row and then grab for next row and subtract
        delta = int(row[1]) - int(prev)
        prev = row[1]
        diff.append(delta)
    #check length
    #print(len(diff))  
    #print(len(date))
    #print(list(diff))  
    #print(date)
    # The total number of months 
    month_count=len(money)
    print("Financal Analysis:")
    print("--------------------")
    print("Total Months: " + str(month_count))

    my_dict = {'x':500, 'y':5874, 'z': 560}

    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

    print('Maximum Value: ',my_dict[key_max])
    print('Minimum Value: ',my_dict[key_min])


    # Import the aperating system module
import os
# Module for reading CSV files
import csv

#Initalize lists and variables
date = []
money = []
total = 0
change = []
total_delta = 0

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    #csv_first_row = next(csvreader)
    #prev = csv_first_row[1]
    #print(prev)
    # Read each row of data after the header to lists
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        total = int(total) + int(row[1]) #calc total profits and losses
        #save prev row and then grab for next row and subtract
        delta = int(row[1]) - int(prev)
        prev = row[1]
        diff.append(delta)
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
    print(len(diff))
    print(len(change))
    print("Average Change: $" + str(avg))
    print("Average Change: $" + str(round(avg))) 
 
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    dictionary = dict(zip(keys, values))
    print(dictionary)

    # The greatest increase in profits (date and amount) over the entire period
    delta_dict = dict(zip(date, diff))
    #print(delta_dict)
    #print(list(delta_dict))
    #full_dict = dict(zip(date, change))
    #print(list(full_dict))
    #print(full_dict)
    max_delta = max(change)
    for x in change:
        if change == max_delta:
            print(x)
    
    #print("Greatest Increase: $" + date[x] + str(max_delta))

    # The greatest decrease in losses (date and amount) over the entire period
    min_delta = min(change)
    print("Greatest Decrease: $" + str(min_delta))