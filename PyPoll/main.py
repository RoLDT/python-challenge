import os
import csv

candidate_options = []
candidate_votes = {}

poll_path = os.path.join("Resources", "election_data.csv")

with open(poll_path, "r") as file:
    csvreader = csv.reader(file, delimiter=",")
    print(csvreader)

    if csv.Sniffer().has_header:
        next(csvreader)   

    for row in csvreader:
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1 

#Finding Total Votes
total_votes = 0
for votes in candidate_votes:
    total_votes = total_votes + candidate_votes[votes]

#Getting the tally
tally = ""
for k, v in candidate_votes.items():
    vote_percent = (v / total_votes)*100
    tally += ((f"{k}: {vote_percent: .3f}% ({v})\n" ))
    winner = max(candidate_votes, key=candidate_votes.get)

#Output
output = (
    f"Election Results\n"
    f"-----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------------\n"
    f"{tally}\n"
    f"-----------------------------\n"
    f"Winner: {winner} \n"
    f"-----------------------------\n"
)
print(output)
output_path = os.path.join("Analysis", "Poll.csv")
with open(output_path, "w") as text_file:
    text_file.write(output)
