import pandas as pd

#using the pandas import to read the csv files needed
dfSalaries = pd.read_csv("Salaries.csv")
dfTeams = pd.read_csv("Teams.csv")

#setting the necessary variable for the project
i = 0
prevYear = 0
prevTeam = ""
totalSalary = 0
highestSalary = 0
highestSalaryTeam = ""
salaryRankSum = 0
averageSalaryRank = 0
highestSalaryRank = 0
lowestSalaryRank = 100
totalYears = 31

#This while loop will run through the entire Salaries csv file 
while i < dfSalaries.shape[0]:
    #from each row set the current year, salary and team equal to what is in the current row
    year = dfSalaries.at[i,"yearID"]
    salary = dfSalaries.at[i,"salary"]
    team = dfSalaries.at[i,"teamID"]

    #check to see if the team is still the same to keep adding the total salary
    if team == prevTeam:
        totalSalary = totalSalary + salary

    #If the team is not the same reset the salaries and check to see if it is the new highest salary of the year
    else:
        if totalSalary > highestSalary:
            highestSalary = totalSalary
            highestSalaryTeam = prevTeam

        totalSalary = salary
        prevTeam = team

    #If the year is different we will end this loop session and figure out what rank the team was for the year who had the highest salary
    if year != prevYear:
        if i == 0:
            prevYear = year
        
        else:
            #print(f"The team with the highest salary in {prevYear} was {highestSalaryTeam} with a salary of {highestSalary}")
            #gets the row that for the year and team with the highest salary
            filteredRow = dfTeams.loc[(dfTeams["yearID"] == prevYear) & (dfTeams["teamID"] == highestSalaryTeam)]
            currentRank = filteredRow["Rank"].values[0]

            salaryRankSum = salaryRankSum + currentRank

            #figuring out the highest rank for the team with the highest salary
            if currentRank > highestSalaryRank:
                highestSalaryRank = currentRank

            #figuring out the highest rank for the team with the lowest salary
            if currentRank < lowestSalaryRank:
                lowestSalaryRank = currentRank

            prevYear = year
            highestSalary = 0
            highestSalaryTeam = ''

    i = i + 1

#gets the average rank for the teams with the highest salary
averageSalaryRank = salaryRankSum / totalYears

#prints out the average, lowest, and highest rank 
print(f"The average rank for team with the highest salary is: {averageSalaryRank:.2f}")
print(f"The best rank for the team with the highest salary is: {lowestSalaryRank}")
print(f"The worst rank for the team with the highest salary is: {highestSalaryRank}")

#reading the Batting csv for the next part
dfBatting = pd.read_csv("Batting.csv")

#getting the rows that are years 1985-2015
filteredRows = dfBatting.loc[(dfBatting["yearID"].isin([1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015]))]

#setting varriable necessary for the next session
prevYear = 1985
prevTeam = ""
mostHits = 0
mostHitsTeam = ""
totalYears = 31
mostHitsRankSum = 0
lowestRanksHits = 100
highestRankHits = 0
averageHitsRank = 0

#setting the row number equal to when the year 1985 starts in the Batting csv
i = dfBatting.shape[0] - filteredRows.shape[0]

#Run through each row of the 
#batting list including years 1985-2015
while i < dfBatting.shape[0]:
    #setting year, hits, and team equal to what is in the row
    year = filteredRows.at[i,"yearID"]
    hits = filteredRows.at[i,"H"]
    team = filteredRows.at[i,"teamID"]

    #See if the current hits is higher than the most hits in a year.
    if hits > mostHits:
        mostHits = hits
        mostHitsTeam = team

    #See if the current year is different and reset from there
    if year != prevYear:
        #Find the row for the team with the player with the most hits in the year
        filteredRow = dfTeams.loc[(dfTeams["yearID"] == prevYear) & (dfTeams["teamID"] == mostHitsTeam)]
        currentRank = filteredRow["Rank"].values[0]

        mostHitsRankSum = mostHitsRankSum + currentRank

        if currentRank > highestRankHits:
            highestRankHits = currentRank

        if currentRank < lowestRanksHits:
            lowestRanksHits = currentRank

        prevYear = year
        mostHits = 0
        mostHitsTeam = ''
        
    i = i + 1

#get the average number rank for the team with the most hits
averageHitsRank = mostHitsRankSum / totalYears

print()
print(f"The average rank for team with the player with the most hits for the year: {averageHitsRank:.2f}")
print(f"The best rank for the team with the highest salary is: {lowestRanksHits}")
print(f"The worst rank for the team with the highest salary is: {highestRankHits}")

