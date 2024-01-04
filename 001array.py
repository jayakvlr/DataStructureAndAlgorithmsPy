expenses=[2200,2350,2600,2130,2190]

#Question 1 -O(1)
a=expenses[1]-expenses[0]
print("In Feb, how many dollars you spent extra compare to January? ",a)
#Question2
sum=0
for i in range(3):
    sum+=expenses[i]
print("Find out your total expense in first quarter (first three months) of the year. ",sum)

#Question 3
print("3. Find out if you spent exactly 2000 dollars in any mon")
if 2000 in expenses:
    print(True)
else:
    print(False)
    
#Question 4
expenses.append(1980)
print("June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list : Use append method",expenses)

#Question 5
expenses[3]=expenses[3]-200
print("Updated April expense",expenses)