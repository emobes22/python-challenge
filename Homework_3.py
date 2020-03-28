# Print Financial Analysis
print("Financial Analysis")
# Print --------------
print("------------------------------")
# Print Total Months:
print("Total Months:")
# Print Total
print("Total:")
# Print Average Change
print("Average Change:")
# Print Greatest Increase in Profits
print("Greatest Increase in Profits:")
# Print Greatest Descrease in Profits
print("Greatest Decrease in Profits:")

#Prints the words in a loop
words = ["Financial Analysis", "--------------------","Total Months:","Total:","Average Change:","Greatest Increase in Profits:","Greatest Decrease in Profits:"]
for word in words:	
	print(word)


print("~~~~~~~~~~~~~~~~~~~~~~~~")
#imports modules to read csvs
import os
import csv

#defines variables
totalmonths=0
totalprofit=0
averagechange=0
dictionary={}

#creates a nickname for the file name & location
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

#reads csv and prints rows
with open(csvpath, 'r') as file_handler:
    reader=csv.reader(file_handler)
    header = next(reader)

    for row in reader:
        dictionary["data"]=row
        print(row)
        totalmonths=totalmonths+1
        print(totalmonths)
        totalprofit=totalprofit+(int(row[1]))
        print(totalprofit)
        averagechange=averagechange-(int(row[1]))
        print(averagechange)
	

print(f"totalmonths: {totalmonths}")
print(f"totalprofit: {totalprofit}")

print(dictionary)
print("~~~~~~~~~~~~~~~~~~~~~~~~")

#for row in csvpath :
#	print (row)
#sum(row)