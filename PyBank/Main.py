import os
import csv
import operator
csv_path = 'C:/Users/nallu/OneDrive/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

temp_csv_path = 'C:/Users/nallu/OneDrive/Desktop/python-challenge/PyBank/Resources/temp.csv'

total_months = 0
row_count = 0
net_profit_loss = int(0) 
highest_profit_row = []
lowest_profit_row = []
previous_profit = 0
final_list = []
total_change = 0
greatest_change = 0
lowest_change = 0
greatest_change_date = 0
lowest_change_date = 0

#open and read from csv file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # pop header from csv reader
    csv_header = next(csv_reader)
    print(csv_header)
    
    for eachrow in csv_reader:
        #calculate the changes in profit/losses for first row v rest of the rows
        if row_count == 0:
            calc_column = 0
            previous_profit = int(eachrow[1])
           
        else:
            calc_column = int(eachrow[1]) - int(previous_profit)

        #prepare new list with column[0] and column[1] from original csv and add calc column as column[3]
        final_list = [eachrow[0], eachrow[1], int(calc_column)]
    
        #for second and subsequent rows
        previous_profit = eachrow[1]   

        #total number of months included in the dataset
        total_months = total_months + 1
        #print(total_months)

        #net total amount of "profit/losses" over the entire period
        net_profit_loss = net_profit_loss + int(eachrow[1])
        #print(eachrow[1])
        #print(net_profit_loss)
        row_count = row_count + 1

        # write final_list content to temp.csv for every row in csvreader
        
        # Open the file using "append" mode, add new row at end of csv file instead of overwriting 
        with open(temp_csv_path, 'a', newline='') as csvfile:

            # Initialize csv.writer
            csvwriter = csv.writer(csvfile, delimiter=',')

            # Write final_list as each row to this csv file
            csvwriter.writerow(final_list)

#open and read from csv file
with open(temp_csv_path) as csv_file:
    temp_csv_reader = csv.reader(csv_file, delimiter=',')
    
    #calculate total change to calculate average change
    for avg_row in temp_csv_reader:
       # print(f"inside total change= {int(avg_row[2])}")
        current_change = int(avg_row[2])
        total_change = total_change + current_change
        
        # calculate greatest increase in profits (date and ammount) over the entire period
        if current_change > greatest_change:     
            greatest_change = current_change
            greatest_change_date =(avg_row[0])

        # calculate greatest decrease in profits (date and ammount) over the entire period
        if current_change < lowest_change:     
            lowest_change = current_change
            lowest_change_date =(avg_row[0])

    print(f"total change= {total_change}")

    #average change
    average_change = round(total_change/total_months, 2)
    print(f"average change = {average_change}")

    
print(f"greatest_change = {greatest_change}")
print(f"greatest_change_date = {greatest_change_date}")
print(f"lowest_change = {lowest_change}")
print(f"lowest_change_date = {lowest_change_date}")

print("--------------------------------------")

#output
txt_output_path = 'C:/Users/nallu/OneDrive/Desktop/python-challenge/PyBank/analysis/output.txt'

# Open the file using "write" mode. Specify the variable to hold the contents
with open(txt_output_path, 'w', newline='') as txtfile:
    
    txtfile.write("Financial Analysis")
    txtfile.write('\n')
    txtfile.write("--------------------------------")
    txtfile.write('\n')
    txtfile.write(f"Total Months: {total_months}")
    txtfile.write('\n')
    txtfile.write(f"Total: {net_profit_loss}")
    txtfile.write('\n')
    txtfile.write(f"Average Change = {average_change}")
    txtfile.write('\n')
    txtfile.write(f"Greatest Increase in Profits: {greatest_change_date}: ({greatest_change})")
    txtfile.write('\n')
    txtfile.write(f"Greatest Decrease in Profits: {lowest_change_date}: ({lowest_change})")

print("--------------------------------------")   

print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_profit_loss}")
print(f"Average Change = {average_change}")
print(f"Greatest Increase in Profits: {greatest_change_date}: ({greatest_change})")
print(f"Greatest Decrease in Profits: {lowest_change_date}: ({lowest_change})")