import os
import csv
import statistics as stat

# input and output paths
csv_path = os.path.join("PyBank", "resources", "budget_data.csv")
out_path = os.path.join("PyBank", "Analysis", "textfile2.txt")

# total months. total amount. counter. list of amount change from row A to row B
mo = 0
am = 0
count = 0
ch = []

with open(csv_path, "r") as file:

    csvreader = csv.DictReader(file, delimiter=',')

    list_of_dict = list(csvreader)

    # initalize two lists for the greatest inc/dec. [Date, Amount]
    great_inc = ["", int(list_of_dict[1]["Profit/Losses"]) - int(list_of_dict[0]["Profit/Losses"])]
    great_dec = ["", int(list_of_dict[1]["Profit/Losses"]) - int(list_of_dict[0]["Profit/Losses"])]

    # row and row_prev(based on count) are used to compare to previous line
    # count is only incremented after the comparison, creating an offset of the rows
    for row in list_of_dict:
        row_prev = list_of_dict[count]
        mo += 1
        am = am + int(row["Profit/Losses"])

        # append ch list with the change from row A to row B
        # skip the first row (check if comparison rows are the equal)
        if row != list_of_dict[0]:
            diff = int(row["Profit/Losses"]) - int(row_prev["Profit/Losses"])
            ch.append(diff)
            if diff > great_inc[1]:
                great_inc[0] = row["Date"]
                great_inc[1] = diff
            if diff < great_dec[1]:
                great_dec[0] = row["Date"]
                great_dec[1] = diff
            count += 1

# print results in terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {mo}")
print(f"Total: ${am}")
print(f"Average Change: ${round(stat.mean(ch),2)}")
print(f"Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})")
print(f"Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})")

# write text file
with open(out_path, 'w') as out:

    out.write("Financial Analysis")
    out.write("\n")
    out.write("----------------------------")
    out.write("\n")
    out.write(f"Total Months: {mo}")
    out.write("\n")
    out.write(f"Total: ${am}")
    out.write("\n")
    out.write(f"Average Change: ${round(stat.mean(ch),2)}")
    out.write("\n")
    out.write(f"Greatest Increase in Profits: {great_inc[0]} (${great_inc[1]})")
    out.write("\n")
    out.write(f"Greatest Decrease in Profits: {great_dec[0]} (${great_dec[1]})")