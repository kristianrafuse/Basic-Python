import os
import csv

# set the path to the CSV file
csvpath = os.path.join(r"PyPoll\Resources\election_data.csv")

# initialize some variables to hold the data we'll be collecting
ballots = [] # list of ballot IDs
candidates = set() # set of candidate names
candidate_votes = {} # dictionary to store the number of votes each candidate receives
total_votes = 0 # total number of votes cast

# open the CSV file and read its contents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the header row
    next(csvreader, None)

    # loop through each row in the CSV file
    for row in csvreader:
        # add the ballot ID to our list of ballots
        ballots.append(row[0])
        # add the candidate name to our set of candidates
        candidates.add(row[2])
        candidate = row[2]

        # if we haven't seen this candidate before, add them to the dictionary of candidate votes
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        # increment the candidate's vote count
        candidate_votes[candidate] += 1
        # increment the total vote count
        total_votes += 1

#print out the results
print(f'There were {total_votes} votes cast in the local election.')
print(f"The following candidates received votes: *{candidates}")

# initialize a variable to keep track of the winning candidate
winner = ''
# initialize a variable to keep track of the winning vote count
winning_votes = 0

# loop through each candidate and print out their percentage of the vote
for candidate in candidate_votes:
    percentage = (candidate_votes[candidate] / total_votes) * 100
    print(f'{candidate}: {percentage:.2f}%')
    print(f'{candidate_votes[candidate]}')

    # check if this candidate has more votes than the current winner
    if candidate_votes[candidate] > winning_votes:
        # if so, update the winning candidate and vote count
        winner = candidate
        winning_votes = candidate_votes[candidate]
        winning_percentage = (winning_votes/total_votes)* 100

# print the winner of the election based on popular vote
print(f'The winner of the election is {winner} with {winning_votes} and {winning_percentage:.2f}% of the popular vote')

# Write the results to a text file
output_path = os.path.join(r"PyPoll\Analysis\election_results.txt")
with open(output_path, "w") as f:
    print("Election Results",file=f)
    print("----------------------------",file=f)
    print(f'Total Votes:{total_votes}',file=f)
    print(f"The following candidates received votes: {candidates}",file=f)
    print("----------------------------",file=f)
    print(f'Winner:{winner}',file=f)

print("PyPoll Assignment complete!")