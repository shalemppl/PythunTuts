# Tuples are similar to lists, but once a tuple is created it cannot be changed

#List (created with [])
mylist = [1, 2, 3]
print(mylist)
mylist[2] = 4
print(mylist)

#Tuple (created with ())
mytuple = (1, 2, 3)
print(mytuple)
#mytuple[2]=4 would result in a traceback, as an item within a tuple cannot be changed

#So why use a tuple instead of a list?
# 1. Tuples are more memory efficient and are faster to access
# 2. CANNOT sort, append or reverse a tuple (as you can with a list)
# 3. CAN count and index a tuple
# 4. Tuples are normally used as temporary variables in limited scopes

#Comparing and Sorting tuples
d = {'a':10, 'b':1, 'c':22} #create a dictionary
d.items()
print(sorted(d.items())) #sort the disctionary (will sort by the first item in the dict first, so a,b,c)

for (k, v) in sorted(d.items()): print(k,v) #create and print a sorted tuple based on the dict

#Sort by the values instead:
tmp = list()
for k,v in d.items(): tmp.append((v,k)) #flip the values, put v first -- notice the double ()
print(tmp)
tmp = sorted(tmp)
print(tmp)
tmp = sorted(tmp,reverse=True) #reverse the order of the items
print(tmp)

#Print the 10 most common words in a file:
fhand = open('intro.txt')
counts = {} #create a dictionary
for line in fhand:
    words = line.split() #split each line in the file into a dictionary of words
    for word in words:
        counts[word] = counts.get(word,0)+1 #for each word, add it to the dict and count it
lst=[] #create a new list
for key,val in counts.items(): #create a tuple containing each pair in the dict we created
    newtup=(val,key) #when creating the tuple, reverse the key/val into val/key so that we can sort by val
    lst.append(newtup) #place the tuple pairs into the list, so we can sort them
lst=sorted(lst,reverse=True) #sort the list, based on val, in reverse (descending) order
for val,key in lst[:10]: #print just the first 10 (most commont) words
    print(key,val)
print('\n')

#A shorter version of the above:
print(sorted([(val,key) for key,val in counts.items()],reverse=True)) #but prints the entire item list, not just the top 10
#the [] creates a "list comprehension"
