#import modules
import os
import csv
# store file location
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# open file in read mode
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Print header
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

    # store length of list in variables for months count
    # lines = len(list(csvreader))

    num_rows = 0
    profit_loss_total = 0
    is_first_row = True

    for row in csvreader:
        # count of months and calculate sum of profit/loss column
        num_rows += 1
        current_month = row[0]
        current_profit = int(row[1])
        profit_loss_total += current_profit
        # Find the max value and month
        if is_first_row:
            is_first_row = False
            max_profit = current_profit
            max_profit_month = current_month
        else:
            if current_profit > max_profit:
                max_profit = current_profit
                max_profit_month = current_month


    print("number of rows:", num_rows)
    print("profit_loss_total:", profit_loss_total)
    

    profit_loss_avg = round(profit_loss_total/num_rows, 2)
    print ("profit_loss_avg:", profit_loss_avg)
    print("max_profit:", max_profit)