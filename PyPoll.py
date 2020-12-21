# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
# REPLACE: file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file from a path
# COMMENT OUR FOR NOW: file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Open the election results and read the file
# REPLACE: election_data = open(file_to_load, 'r')

# New list
candidate_options = []

# Declare empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote vount
        total_votes += 1

        # Print the name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0

        # Increment to count votes
        candidate_votes[candidate_name] += 1

# Determine percentage of votes for each candidate by looping through the counts
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Retrieve vote count of candidates
    votes = candidate_votes[candidate_name]
    # Calc percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate
    # Determine if the votes are greate than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true, then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_cadidate equal to the name
        winning_candidate = candidate_name

    # Print each candidate's name, vote count, and percentage of votes to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Close the file.
# election_data.close()

# Using the with statement, opent he file as a text file
# REPLACE: outfile = open(file_to_save, 'w')
# COMMENT OUT FOR NOW with open(file_to_save, 'w') as txt_file:

# Write
# COMMENT OUT FOR NOW txt_file.write("Counties in the Election\n------------------------------\nArapahoe\nDenver\nJefferson")

# Close file
# COMMENT OUT FOR NOW outfile.close()
