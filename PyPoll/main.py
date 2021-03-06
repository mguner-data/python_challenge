# Import modules 
import os
import csv

# Define the path and read the csv file

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first and skip it
    csv_header = next(csvreader)
   
    vote_counter=0
    candidates_list=[]
    
    # Counting how many people voted and split the candidates list from the csv
    for row in csvreader:
        vote_counter=vote_counter+1
        candidates_list.append(row[2])
        
# Import Counter from collections
# Counting unique values and their frequency by using Counter  
# Reference: https://stackoverflow.com/questions/12282232/how-do-i-count-unique-values-inside-a-list

from collections import Counter
votes=Counter(candidates_list)

# Convert counter to a dictionary
candidate_name_vote_count=dict(votes)
 
# Convert dictionary to two list, one for names; the other for vote counts
   
candidate_name= list(candidate_name_vote_count.keys())  
vote_count=list(candidate_name_vote_count.values())

# Printing output variables to terminal
print("------------------------")
print("Election Results")
print("------------------------")
print(f"Total votes : {vote_counter}")
print("------------------------")

#Print candidate names and respective vote percentages and counts
for i in range(len(candidate_name)):
    print(f' {candidate_name[i]} : {round(((vote_count[i])*100/(vote_counter)),3)} % ({vote_count[i]}) ')

  
index_max_val=vote_count.index(max(vote_count))
print("------------------------")
print(f'Winner : {candidate_name[index_max_val]}')
print("------------------------")

# Write output to txt file
output_path = open('Analysis/election_results.txt', 'w')

output_path.write('Election Results \n')
output_path.write(f'Total votes : {vote_counter} \n')
for i in range(len(candidate_name)):
    output_path.write(f'{candidate_name[i]} : {round(((vote_count[i])*100/(vote_counter)),3)} % ({vote_count[i]}) \n')  
output_path.write(f'Winner: {candidate_name[index_max_val]} \n') 
    
output_path.close()
 

    