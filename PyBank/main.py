#Read Resource CSV
import os
import csv

#Establish Path
budget_path = os.path.join("Resources", "budget_data.csv")

# Total number of months in dataset - CHECK

#Net total amount of "Profit/Losses" over the entire period

#Average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

# Read, open and print CSV file
count_of_months = 0
net_total = 0
dates = []
profits = []
changes = []
profit = 0
last_profit = 0

with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    if csv.Sniffer().has_header:
        next(csvreader)

    for row in csvreader:
        # Total number of months
        count_of_months += 1
        # Net Total Amount of P&Ls
        net_sum = float(row[1])
        net_total += net_sum
        #Average of the changes
        dates.append(str(row[0]))
        profits.append(float(row[1]))

        profit = float(row[1])
        change_in_profit = float(profit) - float(last_profit)
        changes.append(change_in_profit)
        last_profit = profit



total_changes = len(changes)
changes_sum = sum(changes)
changes_average = changes_sum / total_changes

print (count_of_months)
print (net_total)
print(changes_average)