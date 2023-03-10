import os
import csv

budget_csv = os.path.join(r"PyBank\Resources\budget_data.csv")

with open(budget_csv, encoding='utf') as f:
    csvreader = csv.reader(f, delimiter=",")

for row in csvreader:
    print(row)
    

