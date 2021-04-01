import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print ("Election Results")
    print ("-------------------------")

    csv_header = next(csvreader)
    DataListElection = list(csvreader)
    TotalVoted = len(DataListElection)
    print("Total Votes: "+str(TotalVoted))
    print ("-------------------------")

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
    KhanPercentage = 100* KhanVotes/TotalVoted
    CorreyPercentage = 100* CorreyVotes/TotalVoted
    LiPercentage = 100* LiVotes/TotalVoted
    OTooleyPercentage = 100* OTooleyVotes/TotalVoted
    
    KhanRounded = round(KhanPercentage,4)
    CorreyRounded = round(CorreyPercentage,4)
    LiRounded = round(LiPercentage,4)
    OTooleyRounded = round(OTooleyPercentage,4)
     #Khan: 63.000% (2218231)
    print(f"Khan: {str(KhanRounded)}% ({str(KhanVotes)})")
    print(f"Correy: {str(CorreyRounded)}% ({str(CorreyVotes)})")
    print(f"Li: {str(LiRounded)}% ({str(LiVotes)})")
    print(f"O'Tooley: {str(OTooleyRounded)}% ({str(OTooleyVotes)})")
    print ("-------------------------")
    WinnerTotal = max(KhanVotes,CorreyVotes,LiVotes,OTooleyVotes)
    
    FinalTalleyList = []
    FinalTalleyList.append(KhanVotes)
    FinalTalleyList.append(CorreyVotes)
    FinalTalleyList.append(LiVotes)
    FinalTalleyList.append(OTooleyVotes)
    
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

        

        
    
    # print(WhoisWinner)    


    print ("-------------------------")



