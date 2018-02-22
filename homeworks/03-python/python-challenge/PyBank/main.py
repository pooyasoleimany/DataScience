import sys
import csv

# In this challenge, you are tasked with creating a Python script for analyzing the 
# financial records of your company. You will be given two sets of revenue data 
# (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two 
# columns: Date and Revenue. (Thankfully, your company has rather lax standards for 
# accounting so the records are simple.)
class BuddgetData:
    def __init__(self, date, revenue):
        self.Date = date
        self.Revenue = revenue
    def __str__(self):return str.format("{} (${})", self.Date, self.Revenue)

class BuddgetDataLayer:
    def __init__(self, fileAddress):
        self._fileAddress = fileAddress
    def GetBuddgetData(self):
        with open(self._fileAddress, 'r') as file:
            reader = csv.reader(file, delimiter = ',', quotechar = '|')
            next(reader)
            for row in reader:
                yield BuddgetData(row[0], int(row[1]))

# Your task is to create a Python script that analyzes the records to calculate 
# each of the following:
# The total number of months included in the dataset
# The total amount of revenue gained over the entire period
# The average change in revenue between months over the entire period
# The greatest increase in revenue (date and amount) over the entire period
# The greatest decrease in revenue (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)
class FinancialAnalyser:
    def __init__(self, buddgetDataLayer):
        self.BuddgetDataLayer = buddgetDataLayer
        self.TotalMonths = 0
        self.TotalRevenue = 0
        revenueChangeSum = 0
        previousRevenue = None
        maxIncrease = None
        maxDecrease = None
        self.GreatestIncreaseInRevenue = None
        self.GreatestDecreaseInRevenue = None
        change = None
        for b in self.BuddgetDataLayer.GetBuddgetData():
            self.TotalMonths +=  1
            self.TotalRevenue += b.Revenue
            if previousRevenue != None:
                change = b.Revenue - previousRevenue
                revenueChangeSum += abs(change)
            if change != None:
                if maxIncrease == None or maxIncrease < change:
                    self.GreatestIncreaseInRevenue = b
                    maxIncrease = change
                if maxDecrease == None or maxDecrease > change:
                    self.GreatestDecreaseInRevenue = b
                    maxDecrease = change
            previousRevenue = b.Revenue

        self.AverageRevenueChange = 0 if self.TotalMonths <= 1 else revenueChangeSum / (self.TotalMonths - 1)

    def __str__(self): 
        return (
            "Total Months: {} \n" + 
            "Total Revenue: {}\n" + 
            "Average Revenue Change: {}\n" + 
            "Greatest Increase in Revenue: {}\n" + 
            "Greatest Decrease in Revenue: {}"
        ).format(
            self.TotalMonths, 
            self.TotalRevenue, 
            self.AverageRevenueChange, 
            self.GreatestIncreaseInRevenue,
            self.GreatestDecreaseInRevenue
        )

# Your final script must be able to handle any such similarly structured dataset in 
# the future (your boss is going to give you more of these -- so your script has to 
# work for the ones to come). In addition, your final script should both print the 
# analysis to the terminal and export a text file with the results.
def Main(fileName):
    print ("File name : " + fileName)
    dataLayer = BuddgetDataLayer(fileName)
    analizer = FinancialAnalyser(dataLayer)
    print(analizer)

if __name__ == '__main__':
    Main(str(sys.argv[1]))