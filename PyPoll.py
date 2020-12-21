# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
# REPLACE: file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
# REPLACE: election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

# Close the file.
election_data.close()

# Using the with statement, opent he file as a text file
# REPLACE: outfile = open(file_to_save, 'w')
with open(file_to_save, 'w') as txt_file:

    # Write
    txt_file.write("Counties in the Election\n------------------------------\nArapahoe\nDenver\nJefferson")

# Close file
outfile.close()
