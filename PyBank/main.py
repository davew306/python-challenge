import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
     
    print ("Financial Analysis")
    print ("------------------------")
 
    csv_header = next(csvreader)
    DataList = list(csvreader)

    #print (DataList)
    TotalMonths = len(DataList)
    print(f"Total Months: {TotalMonths}")
    
    totalprofits = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    ChangeData=[]
    rownumber = 1
    previousMonth = 0
    
    for row in DataList:    
        totalprofits = totalprofits + int(row[1])
        #print(row)
        #print(rownumber)
        if rownumber > 1:
           ChangeData.append(int(row[1])- previousMonth)
           
           

        #print (row[1])
        rownumber = rownumber +1
        previousMonth = int(row[1])
    
    
    print("Total: $"+str(totalprofits))
    SumData= sum(ChangeData)
    AverageChange = round(SumData/len(ChangeData), 2)
    print("Average Change: $" +str(AverageChange))

#      datalistdictionary = dict.fromkeys(DataList,"List")
#     print(datalistdictionary) 
    
CountM = [i for i in range(1,len(DataList))]
    #print(CountM)
    
    #print(ChangeData)

FirstZip = zip(CountM, ChangeData)
    
    #print (FirstZip)
    

MaxIncrease= max(ChangeData)
MaxDecrease= min(ChangeData)
    #print(MaxIncrease)

for row in FirstZip:
    if row[1] == MaxIncrease:
        MaxItem =row[0]
    elif row[1] ==MaxDecrease:
        MinItem =row[0]
    #print(MaxItem)
MaxObject= DataList[MaxItem]
MinObject= DataList[MinItem]
MaxDate = MaxObject[0]
MinDate = MinObject[0]
print ("Greatest Increase in Profits: "+ MaxDate + " ($"+str(MaxIncrease)+")" )
print ("Greatest Decrease in Profits: "+ MinDate + " ($"+str(MaxDecrease)+")" )






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




  
    
