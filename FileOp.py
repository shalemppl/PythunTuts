# Tutorial at https://www.youtube.com/watch?v=8DvywoWv6fI&t=13580s

#open the file and put it in a handle named "file"
file = open('mbox.txt')
#read each line in the file and print it out
for line in file:
    print(line)

#counting lines in the file
cfile = open('mbox.txt')
count = 0
for line in cfile:
    count = count + 1
print('Line Count:', count)

#read in an entire file at once (instead of by line)
wfile = open('mbox-short.txt')
inp = wfile.read()
print(len(inp))  #print out the legth of the file, in number of characters

#print the first 20 characters of the file
print(inp[:20]) #same as [0:20]

#search through a file
sfile = open('mbox-short.txt')
for line in sfile:
    line = line.rstrip()  #strips the white space (or extra /n) at the end of the lines
    if line.startswith('From:') :
        print(line)

#another way to do it:
sfile2 = open('mbox-short.txt')
for line in sfile2:
    line = line.rstrip()  #strips the white space (or extra /n) at the end of the lines
    if not line.startswith('From:') :
        continue
    print(line)

#and to search for a string in the middle of the line, instead of at the start, use the 'in' operator:
sfile3 = open('mbox-short.txt')
for line in sfile3:
    line = line.rstrip()  #strips the white space (or extra /n) at the end of the lines
    if not '@uct.ac.za' in line :
        continue
    print(line)

#Prompt for a file name:
pfilename = input('Enter a file name: ')
try:                           #The try and except functions make sure that we do not get a traceback if the file is not found
    pfile = open(pfilename)
except:
    print('File ', pfilename, ' cannot be opened or not found.')
    quit ()                     #If the file is not found, the program quits naturally, instead of giving a traceback.  Otherwise the file is opened.
count=0
for line in pfile:
    if line.startswith('Subject:'):
        count = count + 1
print('There are ', count, 'subject lines in ', pfilename)
