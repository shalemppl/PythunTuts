#Finding the most common word in a file (from Dict.py):
fname = input('Enter file name: ')
if fname == '' : fname='clown.txt'
fhandle = open(fname)

di = {}
for line in fhandle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
fhandle.close()

print(di,'\n')

#New code, to find the most common 5 words in the file, which will require sorting:
x=di.items()
print(x, '\n')
x=sorted(di.items())
print(x,'\n')
print(x[:5],'\n')

print('TOP 5:\n')
tmp=[] #create a list
for k,v in di.items():
    print(k,v)
    newtuple=(v,k) #create a tuple while reversing the key/val to val/key
    tmp.append(newtuple)

print(tmp, '\n')

tmp = sorted(tmp,reverse=True)
print('Sorted tmp: ', tmp, '\n')
print('Top 5: ', tmp[:5])

#to print in a nicer format:
for v,k in tmp[:5] : print('Top 5 Nicer: ', k,v)
