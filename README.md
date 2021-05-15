# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to comlete the election audit of a recent local congressional election.

#### 1. Calculate the total number of votes cast.

#### 2. Generate County level election results:
	* Get a complete list of counties in the election
	* Calculate the total number of votes from each county
	* Calculate the percentage of voter trun-out compared to the total number of cotes cast.
	* Determine the county with the highest voter turn-out.

#### 3. Generate Candidate level election results:
	* Get a complete list of candidates who received votes.
	* Calculate the total number of votes each candidate received.
	* Calculate the percentage of votes eacj candidate won.
	* Determine the winner of the election based on popular vote.

## Resources
- Data Source " election_results.csv"
- Python ver 3.7 was used to analyze the data

## Election audit results
	* There are 3 counties in the local region and 3 candidates
	* A total of 369,711 votes were cast in the election
	* Here is the voter turn-out across the counties:
		 -- Jefferson: 10.5% (38,855)
		 -- Denver: 82.8% (306,055)
		 -- Arapahoe: 6.7% (24,801)
	* As you can see 'Denver' county had the lsrgest voter turnout of 306,055.
	
	* Here is a view of the vote spread among the 3 candidates:
		 -- Charles Casper Stockham: 23.0% (85,213)
		 -- Diana DeGette: 73.8% (272,892)
		 -- Raymon Anthony Doane: 3.1% (11,606)
		 
	* Raymon Anthony Doane won the election with a majority of 11,606 votes, 
		which would 73.8% of the total votes cast.

   ![Terminal output screenshot](https://github.com/JoRanjit/Election_Analysis/blob/main/Resources/Terminal%20output%20screenshot.png)
	
## Election audit summary

### The code can be refactored to analyze any elections

#### Pre-requisites:

	1. Create 2 sub-folders in the main folder with the Python code
		* Resources
		* analysis
	2. The data should be uploaded to the 'Resources' folder as a csv file
		- name of the file should be 'election_analysis.csv'
		- should have 3 columns - Ballot ID, County and Candidate
	
#### The code could also be modified to show:

	* The votes received by each candidate from each county
		-- Charles Casper Stockham:
			++ Jefferson: 
			++ Denver: 
			++ Arapahoe: 
		and so on..
		
	* The votes received in a county for each of the candidates.
		-- Jefferson: 
			++ Charles Casper Stockham: 
			++ Diana DeGette: 
			++ Raymon Anthony Doane:
		and so on..
	


