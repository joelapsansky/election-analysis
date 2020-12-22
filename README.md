# Election Analysis
Finished Python Deliverable: [PyPoll Challenge](/PyPoll_Challenge.py)
## Overview of Election Audit
Using Python in VS Code, I completed an audit of a recent congressional election for employees working at the Colorado Board of Elections.

## Resources
This is the csv file containing the dataset (369,712 rows with a header):   
[Election Results](/Resources/election_results.csv)

## Results

For reference, the text file containing the analysis is here: [Election Analysis](/Analysis/election_analysis.txt)  
### Analysis Summary 
* There were 369,711 votes cast
* Denver has the largest turnout
  -Denver:82.8% (306,055)
  -Jefferson:10.5% (38,855)
  -Arapahoe:6.7% (24,801)
* Diane DeGette had the highest number of votes
  -Charles Casper Stockham: 23.0% (85,213)
  -Diana DeGette: 73.8% (272,892)
  -Raymon Anthony Doane: 3.1% (11,606)
	
## Election-Audit Summary

The election commission could easily use this Python Script for other elections.  Assuming formatting of the dataset is the same, the election commission could use this script for a presidential election, or a state election.  They would just have to modify the county variables to say "country" or "state" instead of "county."
     
This script will work on any number of ballots so for any future election that counts results in the same way and outputs a dataset in the same format (i.e. Ballot ID, County, and Candidate in a table), this script can run and give a summary in seconds.
  
On the other hand, if the election commission encounters a situation where they just have candidates and votes with no ballot IDs, they could modify the for statements that contain 'counters,' like this one, for example:  
```
total_votes = total_votes + 1
```
Instead, the commission would have to reference the column with the votes and sum the counts.  
  
If the dataset is the same number of columns, the Script is easily adaptable with minimal changes.  If the dataset is different, but the Script will need additional changes, but it could most likely be adapted more easily than starting from scratch.
  
