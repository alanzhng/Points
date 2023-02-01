import csv
import sys
from datetime import datetime


if len(sys.argv) != 2: sys.exit("Invalid arguments")
records = []                         # List used to hold transactions
spend_points = int(sys.argv[1])      # Points to spend, read from cmdline argument
user_points = 0                      # User total points, calculated while reading CSV file


# Read CSV file and store each transaction in a dict. Append this dict to records
with open('transactions.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    ct = 0
    for row in spamreader:
        if ct == 0:             
            ct += 1
            continue
        datetime_str = row[2].replace("T", " ")[:-1]
        transaction = {'payer': row[0], 'points': int(row[1]), 'timestamp': datetime_str}
        records.append(transaction)
        user_points += int(row[1])
        ct += 1
# Validate that the user has enough points to spend the inputted amount
if spend_points > user_points: sys.exit("Not enough points to spend")
# Sort records by timestamp (using the datetime module)
records.sort(key = lambda x: datetime.strptime(x['timestamp'], '%Y-%m-%d %H:%M:%S'))


# Iterates through the chronological list of records. Subtracts transaction points from the total points to spend. 
# Also handles the edge cases of negative transaction points and when transaction points are greater than the total points to spend.
# Effectively returns what we are looking for: a list with the remaining payers' point balances.
index = 0
while spend_points != 0:
    t_points = records[index]['points']
    if spend_points < t_points:
        records[index]['points'] -= spend_points
        spend_points = 0
    else:
        spend_points -= t_points
        records[index]['points'] = 0
    index += 1


# Iterates through records and calculates the remaining payers' point balances. Formats the results into the specified 
# dictionary to be printed.
output = {}
for r in records:
    output[r['payer']] = output.get(r['payer'], 0) + r['points']
print(output)
