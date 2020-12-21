# Add our dependencies

import csv
import os

# Assign a variable to load a file from a path
# REPLACE: file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file from a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file
# REPLACE: election_data = open(file_to_load, 'r')
# Initialize a total vote counter
total_votes = 0
# New list candidate options
candidate_options = []
# Declare empty dictionary candidate votes
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

# Save results to text file
# REPLACE: outfile = open(file_to_save, 'w')
with open(file_to_save, 'w') as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    # Comment out: print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

# Determine percentage of votes for each candidate by looping through the counts
# Iterate through candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of candidates
        votes = candidate_votes[candidate_name]

        # Calc percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

         # Put candidate results in variable
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal
        # Comment out: print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determine if the votes are greate than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true, then set winning_count = votes and winning_percentage = vote_percentage and winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print each candidate's name, vote count, and percentage of votes to terminal
    # Comment out: print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # Comment out: print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    
# Close the files
election_data.close()
txt_file.close()