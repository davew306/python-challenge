import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
     
    print ("Financial Analysis")
    print ("------------------------")
    #store the header as a variable
    csv_header = next(csvreader)

    #storing the csv file to a list
    DataList = list(csvreader)

    #Finding the length of the Data List
    TotalMonths = len(DataList)
    print(f"Total Months: {TotalMonths}")
    
    totalprofits = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    ChangeData=[]
    rownumber = 1
    previousMonth = 0
    
    #Summing the total difference in profits
    for row in DataList:    
        totalprofits = totalprofits + int(row[1])
    #Creating a list of Change Data
        if rownumber > 1:
           ChangeData.append(int(row[1])- previousMonth)
           
           

    
        rownumber = rownumber +1
        previousMonth = int(row[1])
    
    
    print("Total: $"+str(totalprofits))
    
    #Average profit
    SumData= sum(ChangeData)
    AverageChange = round(SumData/len(ChangeData), 2)
    print("Average Change: $" +str(AverageChange))
    
    # Creating an index for the Change Data 
CountM = [i for i in range(1,len(DataList))]
    #CountM and ChangeData are the same length

#Zipping the two lists to a tuple
FirstZip = zip(CountM, ChangeData)
    
    
#Finding the Max increase and decrease amount and storing them as variables
MaxIncrease= max(ChangeData)
MaxDecrease= min(ChangeData)

#Storing the Max increase and decrease index as variable
for row in FirstZip:
    if row[1] == MaxIncrease:
        MaxItem =row[0]
    elif row[1] ==MaxDecrease:
        MinItem =row[0]

#Finding the dates of the Max increase and decrease and storing them as variables
MaxObject= DataList[MaxItem]
MinObject= DataList[MinItem]
MaxDate = MaxObject[0]
MinDate = MinObject[0]
print ("Greatest Increase in Profits: "+ MaxDate + " ($"+str(MaxIncrease)+")" )
print ("Greatest Decrease in Profits: "+ MinDate + " ($"+str(MaxDecrease)+")" )





#Output to a txt file the Printed string 
import sys   
original_stdout = sys.stdout

with open('analysis/Financial.txt', 'w') as f:
    sys.stdout = f 
    print ("Financial Analysis")
    print ("------------------------")
    print(f"Total Months: {TotalMonths}")
    print("Total: $"+str(totalprofits))
    print("Average Change: $" +str(AverageChange))
    print ("Greatest Increase in Profits: "+ MaxDate + " ($"+str(MaxIncrease)+")" )
    print ("Greatest Decrease in Profits: "+ MinDate + " ($"+str(MaxDecrease)+")" )
    sys.stdout = original_stdout




  
    
