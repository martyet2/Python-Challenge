import csv

# file path
csvpath = "Resources/budget_data.csv"

# set variables
month_count = 0
total_profit = 0
changes = []

# open the csv
with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row after the header
    for row in csvreader:
        print(row)

        # count months
        month_count += 1

        # add profit
        total_profit += int(row[1])

        # if first row, there is no change
        if month_count == 1:
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)

            # reset last month profit
            last_month_profit = int(row[1])

    print(month_count)
    print(total_profit)

    avg_change = sum(changes) / len(changes)
    print(avg_change)

    max_change = max(changes)
    max_month_indx = changes.index(max_change)
    max_month = max_month_indx + 1

    print(max_change)
    print(max_month)

    min_change = min(changes)
    min_month_indx = changes.index(min_change)
    min_month = min_month_indx + 1

    print(min_change)
    print(min_month)

# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: {avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_month} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_change})\n")
# Print the output (to terminal)
print(output)
# Export the results to text file
with open("budget_analysis.txt", "w") as txt_file:
    txt_file.write(output)



