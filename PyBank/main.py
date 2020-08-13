#Read Resource CSV
import os
import csv

#Establish Path
#budget_path = os.path.join("Resources", "budget_data.csv")
budget_path = "C:\\Users\\Rodrigo Lozano\\Desktop\\DATABOOTCAMP\\Tarea\\Tarea3_Python\\python-challenge\\PyBank\\Resources\\budget_data.csv"

count_of_months = 0
net_total = 0
dates = []
profits = []
changes = []
profit = 0
last_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

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

        if change_in_profit > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change_in_profit

        if change_in_profit < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change_in_profit


total_changes = len(changes)-1
changes_sum = sum(changes[1:])
changes_average = changes_sum / total_changes

output = (
    f"Financial Analysis\n"
    f"------------------------\n"
    f"Total Months: {count_of_months}\n"
    f"Total: {net_total}\n"
    f"Average Change: ${changes_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n"
)
output_path = "C:\\Users\\Rodrigo Lozano\\Desktop\\DATABOOTCAMP\\Tarea\\Tarea3_Python\\python-challenge\\PyBank\\Analysis\\TEST_OUTPUT.CSV"
with open(output_path, "w") as text_file:
    text_file.write(output)
print(output)
