# Summing a Million
#
# Make a list of the numbers from one to one million, 
#  and then use min() and max() to make sure your list actually strats at one and ends at one million. 
# Also,use the sum function to see how quickly Python can add a million numbers.

million = list(range(1,(1*10**6+1)))
print (min(million))
print (max(million))
print (sum(million))