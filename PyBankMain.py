import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
     
    print ("Financial Analysis")
    print ("------------------------")
 
    csv_header = next(csvreader)
    DataList = list(csvreader)
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
           #print(ChangeData)
           

        #print (row[1])
        rownumber = rownumber +1
        previousMonth = int(row[1])
    print("Total: $"+str(totalprofits))
    SumData= sum(ChangeData)
    AverageChange = round(SumData/len(ChangeData), 2)
    print("Average Change: $" +str(AverageChange))
    


  
    

    
    