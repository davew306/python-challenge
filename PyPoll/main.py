import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print ("Election Results")
    print ("-------------------------")
    #storing the header as a variable
    csv_header = next(csvreader)

    #storing the read data as a list to variable DataListElection
    DataListElection = list(csvreader)
    TotalVoted = len(DataListElection)
    print("Total Votes: "+str(TotalVoted))
    print ("-------------------------")
# Counting the votes for each candidate
    KhanVotes = 0
    CorreyVotes = 0
    LiVotes = 0
    OTooleyVotes = 0
    for row in DataListElection:
        if row[2] == "Khan":
            KhanVotes= KhanVotes +1 
        elif row[2] == "Correy":
            CorreyVotes= CorreyVotes +1
        elif row[2] == "Li":
            LiVotes= LiVotes +1
        elif row[2] == "O'Tooley":
            OTooleyVotes = OTooleyVotes +1
    #calculating the percentages of the votes for each candidate
    KhanPercentage = 100* KhanVotes/TotalVoted
    CorreyPercentage = 100* CorreyVotes/TotalVoted
    LiPercentage = 100* LiVotes/TotalVoted
    OTooleyPercentage = 100* OTooleyVotes/TotalVoted
    
    KhanRounded = round(KhanPercentage,3)
    CorreyRounded = round(CorreyPercentage,3)
    LiRounded = round(LiPercentage,3)
    OTooleyRounded = round(OTooleyPercentage,3)
    
    print(f"Khan: {str(KhanRounded)}% ({str(KhanVotes)})")
    print(f"Correy: {str(CorreyRounded)}% ({str(CorreyVotes)})")
    print(f"Li: {str(LiRounded)}% ({str(LiVotes)})")
    print(f"O'Tooley: {str(OTooleyRounded)}% ({str(OTooleyVotes)})")
    print ("-------------------------")
    
    #Finding the total for the Winner
    WinnerTotal = max(KhanVotes,CorreyVotes,LiVotes,OTooleyVotes)
    #Creating a list of the final talley of the Votes for each candidate
    FinalTalleyList = []
    FinalTalleyList.append(KhanVotes)
    FinalTalleyList.append(CorreyVotes)
    FinalTalleyList.append(LiVotes)
    FinalTalleyList.append(OTooleyVotes)
    #determining the winner
    for row in FinalTalleyList:
        if WinnerTotal == KhanVotes:
                Winner = "Khan"
        elif WinnerTotal == CorreyVotes:
                Winner = "Correy"
        elif WinnerTotal == LiVotes:
                Winner = "Li"
        elif WinnerTotal == OTooleyVotes:
                Winner = "O'Tooley"
    print(f"Winner: {Winner}")

        

        
        
print ("-------------------------")

#output txt file of the printed strings
import sys   
original_stdout = sys.stdout

with open('analysis/FinalElection.txt', 'w') as f:
    sys.stdout = f 
    print ("Election Results")
    print ("-------------------------")
    print("Total Votes: "+str(TotalVoted))
    print ("-------------------------")
    print(f"Khan: {str(KhanRounded)}% ({str(KhanVotes)})")
    print(f"Correy: {str(CorreyRounded)}% ({str(CorreyVotes)})")
    print(f"Li: {str(LiRounded)}% ({str(LiVotes)})")
    print(f"O'Tooley: {str(OTooleyRounded)}% ({str(OTooleyVotes)})")
    print ("-------------------------")
    print(f"Winner: {Winner}")
    print ("-------------------------")
    sys.stdout = original_stdout
