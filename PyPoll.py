# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
 
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")  

# 1. Initialize a total vote counter.
total_votes = 0

#intialize candidate_options
candidate_options = []

#intialize dictionary 
candidate_votes = {}

#intialize winning count and cadidate
winning_count=0
winning_percentage = 0
winning_candidate = ""

# Open the election results and read the file.
with open(file_to_load) as election_data:
     # To do: read and analyze the data here
     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)     
     # Print header row in the CSV file.
     headers = next(file_reader)
    
     #1. Total number of votes cast
     #2. A complete list of candidates who received votes
     #3. Total number of votes each candidate received
     for row in file_reader:
          total_votes +=1
          candidate_name = row[2]
          #check and add if candidate name's already in the list
          if candidate_name not in candidate_options:
               #add it to the list
               candidate_options.append(candidate_name)
               candidate_votes[candidate_name]=0
          # add a vote to that candidate
          candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
     for candidate_name in candidate_votes:
           # Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          vote_percentage = (float(votes)/float(total_votes))*100

          # To do: print out each candidate's name, vote count, and percentage of
          # votes to the terminal.
          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

          # Determine winning vote count and candidate
          # 1. Determine if the votes are greater than the winning count.
          if votes > winning_count and vote_percentage > winning_percentage:
          # 2. If true then set winning_count = votes and winning_percent =
          # vote_percentage.
               winning_candidate = candidate_name # 3. Set the winning_candidate equal to the candidate's name.
               winning_count = votes
               winning_percentage = vote_percentage
     
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
    
     for candidate in candidate_votes:
          winning_candidate_summary = (
               f"----------------------------------\n"
               f"Winner: {winning_candidate} \n"
               f"Winning Vote Count: {winning_count:,}\n"
               f"Winning Percntage: {winning_percentage:.1f}% \n "
               f"-----------------------------------\n"
          )
     print(winning_candidate_summary)