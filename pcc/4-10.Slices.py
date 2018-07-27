# Slices
#
# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following
# - print the message, the first three items in the list are:.
# Then use a slice to print the first three items from that program's list.
# - print the message, three items from the middle of the list are:.
# Use a slice to print three items from the middle of the list.
# - print the message, the last three items in the list are:.
# Use a slice to print the last three items in the list.

threes = list(range(3,30,3))

print("The first three items in the list are: " + str(threes[:3]))

mid = len(threes)//2
print("Three items from the middle of the list are: " + str(threes[mid-1:mid+2]))

print("The last three items in the list are: " + str(threes[-3:]))