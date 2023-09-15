import csv
import os

# open csv as list

with open(os.path.join('Resources', 'budget_data.csv')) as csvfile:
        budget_data = list(csv.reader(csvfile, delimiter=','))
        budget_data.pop(0)

# define variables

months = 0
total = 0
change_list = []
prev_value = 0
max_inc_value = 0
max_inc_month = ""
max_dec_value = 0
max_dec_month = ""

# count total number of months
# calculate net total profit/loss

for row in budget_data:
    months += 1
    total += int(row[1])

    # calculate monthly changes
    # identify greatest monthly increase and decrease
    
    change = int(row[1])-int(prev_value)
    change_list.append(change)
    prev_value = row[1]
    if change > max_inc_value:
         max_inc_value = change
         max_inc_month = row[0]
    elif change < max_dec_value:
         max_dec_value = change
         max_dec_month = row[0]

# calculate average month to month change

change_list.pop(0)
x = 0
for i in change_list:
    x += i
ave_change = round((x/len(change_list)), 2)

# format results

fin_analysis = ("\n"
"Financial Analysis\n"
"------------------------------------\n"
f"Total Months: {months}\n"
f"Total: ${total}\n"
f"Average Change: ${ave_change}\n"
f"Greatest Increase in Profits: {max_inc_month} (${max_inc_value})\n"
f"Greatest Decrease in Profits: {max_dec_month} (${max_dec_value})"
)
print(fin_analysis)

# write results to .txt

with open(os.path.join('analysis', 'budget_analysis.txt'), 'w') as f:
     f.writelines(fin_analysis)
