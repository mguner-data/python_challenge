# Import modules 
import os
import csv

# Read the csv file

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first and skip it
    csv_header = next(csvreader)
   
    # n is the variable for month counter
    # Calculate net total amount of Profit/Losses
    # initialize empty counters and empty lists to hold month counter, total profit and Profit/Loss Column
    n=0
    net_total_profit=0
    new_list_pro_loss=[]
    new_list_months=[]
    
# iterating in the csv file rows except the header row

    for row in csvreader:
        
        n=n+1
        net_total_profit = net_total_profit + float(row[1])
        new_list_months.append(row[0])
        new_list_pro_loss.append(row[1])

# a new list named as change holding month to month change in profit/loss
change = [float(new_list_pro_loss[i+1])-float(new_list_pro_loss[i]) for i in range(len(new_list_pro_loss)-1)]
average_change = round(float(sum(change)/len(change)),2)

# Find the minimum and maximum changes in the list change    

max_val=int(max(change))
index_max = change.index(max(change))
min_val=int(min(change))
index_min=change.index(min(change))

print(f'------------------------------------------')
print(f'Financial Analysis')
print(f'------------------------------------------')
print(f'Total Months : {n} ')
print(f'Total : $ {round(net_total_profit)}')
print(f'Average Change : $ {average_change}')
print(f'Greatest Increase in Profits : {new_list_months[index_max+1]} (${max_val})')
print(f'Greatest Decrease in Profits : {new_list_months[index_min+1]} (${min_val})')

# Write output to txt file
output_path = open('Analysis/financial_analysis.txt', 'w')

output_path.write('Financial Analysis \n')
output_path.write(f'Total Months : {n} \n')
output_path.write(f'Total : $ {net_total_profit} \n')  
output_path.write(f'Average Change : $ {average_change} \n')
output_path.write(f'Greatest Increase in Profits : {new_list_months[index_max+1]} (${max_val}) \n')
output_path.write(f'Greatest Decrease in Profits : {new_list_months[index_min+1]} (${min_val}) \n')
    
output_path.close()
    


