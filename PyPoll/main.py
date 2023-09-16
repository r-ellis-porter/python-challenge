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
results.append(count)
results.append(format(count/len(candidates), ".3%"))
all_results.append(results)
all_results.pop(0)
if count > top_votes:
    top_votes = count
    winner = prev_row

# count total votes

total_votes = len(candidates)

# format results

election_results = ("\n"
"Election Results \n"
"---------------------------\n"
f"Total Votes: {total_votes}\n"
"---------------------------\n"
f"{all_results[0][0]}: {all_results[0][2]} ({all_results[0][1]})\n"                  
f"{all_results[1][0]}: {all_results[1][2]} ({all_results[1][1]})\n"
f"{all_results[2][0]}: {all_results[2][2]} ({all_results[2][1]})\n"
"---------------------------\n" 
f"Winner: {winner}\n"
"---------------------------"                  
)
print(election_results)

# write results to .txt

with open(os.path.join('analysis', 'election_analysis.txt'), 'w') as f:
    f.writelines(election_results)