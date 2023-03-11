import os
import csv

csvpath = os.path.join(r"PyPoll\Resources\election_data.csv")

ballots = []
candidates = set()
candidate_votes = {}
total_votes = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        ballots.append(row[0])
        candidates.add(row[2])
        candidate = row[2]

        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1
        total_votes += 1


total_votes = len(ballots)
candidate_list = list(candidates)

print(f'There were {total_votes} votes cast.')
print(f"The following candidates received votes: {candidate_list}")

for candidate in candidate_votes:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    print(f'{candidate}: {percentage:.2f}%')

