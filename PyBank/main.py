# Import the necessary modules
import os
import csv

# Set the file path for the budget data CSV file
csvpath = os.path.join(r"PyBank\Resources\budget_data.csv")

# Create empty lists to store the dates, months, profits, and total.
dates =[]
months = []
profits = []
total =[]

# Open the CSV file and read the rows into the lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # Skip over/store the header row!

    for row in csvreader:
        dates.append(row[0])
        profits.append(int(row[1]))

# Calculate the total number of months in the dataset and the total amount of profits for the entire period
months = len(dates)
total = sum(profits)

# Calculate the changes in profits from month to month and store them in a list
profit_loss = []
for i in range(1, len(profits)):
    change = profits[i] - profits[i-1]
    profit_loss.append(change)

# Calculate the total change in profits and the average change in profits from month to month. Took me a minute to realize the changes would be (month -1), not just month!
pl_total = sum(profit_loss)
pl_avg = round(pl_total / (months-1), 2)

# Find the greatest increase and greatest decrease in profits, along with their respective dates
max_increase = max(profit_loss)
max_increase_index = profit_loss.index(max_increase)
max_increase_date = dates[max_increase_index+1]
max_increase_amount = max_increase

max_decrease = min(profit_loss)
max_decrease_index = profit_loss.index(max_decrease)
max_decrease_date = dates[max_decrease_index+1]
max_decrease_amount = max_decrease

# Print the results to the terminal
print("Total Months:",months)
print("Total:$",total)
print("Average Change:$",pl_avg)
print("Greatest Increase in Profits:",max_increase_date,"($",max_increase_amount,")")
print("Greatest Decrease in Profits:",max_decrease_date, "($",max_decrease_amount,")")

# Write the results to a text file -- Is there a quicker way to do this? 
output_path = os.path.join(r"PyBank\Analysis\financial_analysis.txt")
with open(output_path, "w") as f:
    print("Financial Analysis",file=f)
    print("----------------------------",file=f)
    print("Total Months:",months, file=f)
    print("Total:$",total, file=f)
    print("Average Change:$",pl_avg, file=f)
    print("Greatest Increase in Profits:",max_increase_date,"($",max_increase_amount,")", file=f)
    print("Greatest Decrease in Profits:",max_decrease_date, "($",max_decrease_amount,")", file=f)

# PyBank Assignment complete!