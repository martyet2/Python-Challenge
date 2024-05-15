# import modules
import csv

# set up path to data set
csvpath = "Resources/election_data.csv"

# set variables
vote_count = 0
candidate_dict = {}

# open the file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # read each row after the header
    for row in csvreader:
        # count the votes
        vote_count += 1

        # add to the dictionary
        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1

print(vote_count)
print(candidate_dict)

# print output
output = f"""Election Results
------------------------------
Total Votes: {vote_count}
------------------------------
"""

max_cand = ""
max_votes = 0

for candidate in candidate_dict.keys():
    # get votes
    votes = candidate_dict[candidate]
    perc = 100 * (votes / vote_count)

    line = f"{candidate}: {round(perc, 3)}% ({votes})"
    output += line

    # get max of dictionary
    if votes > max_votes:
        max_cand = candidate
        max_votes = votes

last_line = f"""----------------------
Winner: {max_cand}
==========================="""

output += last_line
print(output)

# used xpert to help with syntax error





 
