# Using a dictionary to count (histogram)
mydict = {} #creates an empty disctionary; same as mydict = dict()
names = ['Ella', 'Hava', 'David', 'Hava', 'Ella', 'Ella']
for name in names:
    if name not in mydict:
        mydict[name] = 1   #if the name is not in the dictionary, add it and set it to 1
    else :
        mydict[name] = mydict[name] + 1  #if the name i already in the dict, add 1 to it
print(mydict)

#Do the same thing using the Get method:
mynewdict = {}
newnames = ['Ella', 'Hava', 'David', 'Hava', 'Ella', 'Ella']
for newname in newnames:
    mynewdict[newname] = mynewdict.get(newname, 0) + 1
    #if newname is not in dict add it with default value of 0, otherwise add 1 to it
    #notice that when a new name is added, it is set to 0 and then immediately 1 is added, so a newly added name is initially set to 1
print(mynewdict)

print(list(mynewdict))
print(mynewdict.keys())
print(mynewdict.values())
print(mynewdict.items())

for x,y in mynewdict.items():
    print(x,y)
