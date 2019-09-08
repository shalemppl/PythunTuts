# Setting up a list (array) and then changing one of the values:
lotto = [1,2,3,4,5]
print(lotto)
lotto[2]=6 #changes the '3' to a '6' (remember, the positions in the array start with 0)
print (lotto)
print('Number of items is ', len(lotto), '\n') #print the number of items in the list

Kids = ['Ella', 'Hava', 'David']
#to print each item in the list:
for kid in Kids:
    print(kid)
#but if we need to know our position in the list as we are printing it:
for i in range(len(Kids)):
    kid = Kids[i]
    print('Kid Number ', i, " is ", kid, '\n')

# Concatenating lists using +
a = [1,2,3]
b = [4,5,6]
c = a + b
print('List A: ', a)
print('List B: ', b)
print('List C: ', c, '\n')

# Printing a slice of a list:
print(c[1:3]) #print the items in position 1 thgrough but not including 3 (so 1 and 2)
print(c[:3]) #print from the beginning until but not including 3
print(c[:]) #print all of c, same as print(c)
print(c[3:], '\n') #print from item 3 to the end

# Builduing a list:
stuff = list()
stuff.append('books') #add an item to the list
stuff.append(99) #lists can contain items of different types, such as strings and integers
stuff.append('turtles')
print(stuff, '\n')

# Creating a list from a string:
mystring = 'This is my string'
mylist = mystring.split() #the default delimiter in creating a list from a string is a space
print(mylist)
print('Position 2 is: ', mylist[2], '\n')

mynewstring = 'this;is;a;new;string'
mynewlist = mynewstring.split()
print(mynewlist, ' ', len(mynewlist))
myupdatedlist = mynewstring.split(';') #now a ; will be used as the delimiter
print(myupdatedlist, ' ', len(myupdatedlist))
