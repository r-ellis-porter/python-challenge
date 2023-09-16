import csv
import os

# open csv as list

with open(os.path.join('Resources', 'election_data.csv')) as csvfile:
    election_data = list(csv.reader(csvfile, delimiter=','))
    election_data.pop(0)

# define variables

candidates = []
count = 1
results = []
all_results = []
prev_row = ""
winner = ""
top_votes = 0

# list and sort votes by candidate name

for vote in election_data:
    candidates.append(vote[2])
candidates.sort()

# calculate total votes and percent won for each candidate
# find candidate with most votes

for i in candidates:
    if i == prev_row:
        count += 1
        if i not in results:
            results.append(i)
    else:
        results.append(count)
        results.append(format(count/len(candidates), ".3%"))
        all_results.append(results)
        if count > top_votes:
            top_votes = count
            winner = prev_row
        count = 1
        results = []
        prev_row = i

# final candidate in list
results.append(count)
results.append(format(count/len(candidates), ".3%"))
all_results.append(results)
all_results.pop(0)
if count > top_votes:
    top_votes = count
    winner = prev_row

# count total votes

total_votes = len(candidates)

# create and format results list of strings

election_results = "\nElection Results\n" + "-" * 25 + "\n"
election_results += f"Total Votes: {total_votes}\n" + "-" * 25 + "\n"
for info in all_results:
    name, percentage, total = info
    election_results += f"{name}: {total} ({percentage})\n"
election_results += "-" * 25 + "\n"
election_results += f"Winner: {winner}\n"
election_results += "-" * 25

print(election_results)

# write results to .txt

with open(os.path.join('analysis', 'election_analysis.txt'), 'w') as f:
    f.writelines(election_results)