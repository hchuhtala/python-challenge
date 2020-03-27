# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

from collections import Counter

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

id = []
county = []
candidate = []
c_total = 0
percent = []


# Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        
    dict = {zip(id, county, candidate)}
    print(dict)
  #The total number of votes cast
    total = len(id)
    print("Election Results:")
    print("--------------------")
    print("Total Number of Votes: " + str(total))
    print("--------------------")

  #A complete list of candidates who received votes
    candidate_set = set(candidate)
    candidate_unique = list(candidate_set)
    n = len(candidate_unique)
    print(candidate_unique[0])
    #print(candidate_set[0])

  #The total number of votes each candidate won
    dict(vote_totals) = Counter(candidate)
    print(vote_totals)
    #for x in candidate:
      #if candidate == candidate_unique[0]:
        #c_total = c_total + 1
      #print(c_total)

  #The percentage of votes each candidate won
    for v in range(n):
      for k, v in vote_totals
        percent.append(vote_totals[v] / total * 100)
    
    k_percent = vote_totals["Khan"] / total * 100
    print(round(k_percent))

  #The winner of the election based on popular vote.
  #Print results
   # print({vote_totals[]})        
