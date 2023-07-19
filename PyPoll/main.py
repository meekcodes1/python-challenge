import os
import csv

# input and output paths
csv_path = os.path.join("PyPoll", "resources", "election_data.csv")
out_path = os.path.join("PyPoll", "analysis", "textfile.txt")

# dictionary for candidates. counter. variable for storing winner
cands = {}
c = 0
winner = ""

with open(csv_path, "r") as file:

    csvreader = csv.DictReader(file, delimiter=',')

    list_of_dict = list(csvreader)

    # Fill new dictionary with only unique candidates. 
    # Sum c for total vote count
    for row in list_of_dict:
        if row["Candidate"] not in cands:
                cands[row["Candidate"]] = 0
        c += 1

    # For each candidate, loop through all rows of file
    # Sum if row value matches candidate
    for cand in cands:
        for row in list_of_dict:
            if row["Candidate"] == cand:
                 cands[cand] = cands[cand] + 1
        
# determine winner
# reference used: https://datagy.io/python-get-dictionary-key-with-max-value/
winner = max(cands, key=cands.get)

# print results in terminal
print("Election Results")
print("-------------------------")
print("Total Votes: "+str(c))
print("-------------------------")
for cand in cands:
    print(f"{cand}: {round(((cands[cand]/c)*100),3)}% ({cands[cand]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# write text file
with open(out_path, 'w') as out:
    out.write("Election Results")
    out.write("\n")
    out.write("-------------------------")
    out.write("\n")
    out.write("Total Votes: "+str(c))
    out.write("\n")
    out.write("-------------------------")
    out.write("\n")
    for cand in cands:
        out.write(f"{cand}: {round(((cands[cand]/c)*100),3)}% ({cands[cand]})")
        out.write("\n")
    out.write("-------------------------")
    out.write("\n")
    out.write(f"Winner: {winner}")
    out.write("\n")
    out.write("-------------------------")