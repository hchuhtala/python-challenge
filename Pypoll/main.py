# import the os module
import os
# Module for reading CSV files
import csv
from collections import Counter

# Specify the file to read
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Specify the file to write to
output_path = os.path.join("election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
txtfile = open(output_path, 'w')

id = []
county = []
candidate = []
c_total = 0
percent = []

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
#The total number of votes cast
total = len(id)

print("Election Results:")
print("--------------------")
print("Total Number of Votes: " + str(total))
print("--------------------")
print("Results by Number of Votes:")
print("--------------------")

txtfile.write("Election Results:\n")
txtfile.write("--------------------\n")
txtfile.write("Total Number of Votes: " + str(total) + "\n")
txtfile.write("--------------------\n")
txtfile.write("Results by Number of Votes:\n")
txtfile.write("--------------------\n")

#A complete list of candidates who received votes and the total number of votes they got
vote_totals = Counter(candidate)
vote_totals_dict = dict(vote_totals)

#The percentage of votes each candidate won
for k, v in vote_totals_dict.items():
  percent.append(round(v / total * 100))
  print(k ,v )
  txtfile.write(str(k) + " " + str(v) + "\n")

vote_percent = dict(zip(vote_totals, percent))

print("--------------------")
print("Results by Percent of Votes:")
print("--------------------")

txtfile.write("--------------------\n")
txtfile.write("Results by Percent of Votes:\n")
txtfile.write("--------------------\n")

for k, v in vote_percent.items():
  print(k ,v )  
  txtfile.write(str(k) + " " + str(v) + "\n")

#The winner of the election based on popular vote.
winner = max(vote_totals_dict.keys(), key=(lambda k: vote_totals_dict[k]))

print("--------------------")
print("Election Winner: ")
print("--------------------")
print (winner)
print()

txtfile.write("--------------------\n")
txtfile.write("Election Winner:\n")
txtfile.write("--------------------\n")
txtfile.write(str(winner))
