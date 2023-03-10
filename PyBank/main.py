import os
import csv

csvpath = os.path.join(r"PyBank\Resources\budget_data.csv")

dates =[]
months = []
profits = []
total =[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        dates.append(row[0])
        profits.append(int(row[1]))

months = len(dates)
total = sum(profits)

profit_loss = []
for i in range(1, len(profits)):
    change = profits[i] - profits[i-1]
    profit_loss.append(change)

pl_total = sum(profit_loss)
pl_avg = round(pl_total / (months-1), 2)

max_increase = max(profit_loss)
max_increase_index = profit_loss.index(max_increase)
max_increase_date = dates[max_increase_index+1]
max_increase_amount = max_increase

max_decrease = min(profit_loss)
max_decrease_index = profit_loss.index(max_decrease)
max_decrease_date = dates[max_decrease_index+1]
max_decrease_amount = max_decrease

print("Total Months:",months)
print("Total:$",total)
print("Average Change:$",pl_avg)
print("Greatest Increase in Profits:",max_increase_date,"($",max_increase_amount,")")
print("Greatest Decrease in Profits:",max_decrease_date, "($",max_decrease_amount,")")

output_path = os.path.join(r"PyBank\Analysis\financial_analysis.txt")
with open(output_path, "w") as f:
    print("Financial Analysis",file=f)
    print("----------------------------",file=f)
    print("Total Months:",months, file=f)
    print("Total:$",total, file=f)
    print("Average Change:$",pl_avg, file=f)
    print("Greatest Increase in Profits:",max_increase_date,"($",max_increase_amount,")", file=f)
    print("Greatest Decrease in Profits:",max_decrease_date, "($",max_decrease_amount,")", file=f)