# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Loaded and output files
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "finanical_analysis.txt")

# Define variables to track the financial data
month_count = 0
total_profit = 0
months = []
net_changes = []

# Add more variables to track other necessary financial data
greatest_increase = {"month": "", "change": 0}
#Floating infinity
greatest_decrease = {"month": "", "change": float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    month_count += 1

    # Track the total and net change
    total_profit += int(first_row[1])
    previous_net = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        month_count += 1
        current_net = int(row[1])
        total_profit += current_net

        # Track the net change
        monthly_change = current_net - previous_net
        previous_net = current_net
        
        months.append(row[0])
        net_changes.append(monthly_change)

        # Calculate the greatest increase in profits (month and amount)
        if monthly_change > greatest_increase["change"]:
            greatest_increase["month"] = row[0]
            greatest_increase["change"] = monthly_change

        # Calculate the greatest decrease in losses (month and amount)
        if monthly_change < greatest_decrease["change"]:
            greatest_decrease["month"] = row[0]
            greatest_decrease["change"] = monthly_change


# Calculate the average net change across the months
average_change = sum(net_changes) / len(net_changes)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total Net Profit: ${total_profit}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['change']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['change']})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
