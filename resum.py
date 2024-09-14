import re
fname=input("Enter file name:")
file=open(fname,'r')
line=file.read()
y=re.findall('[0-9]+',line)
lst=list(map(int,y))
total=sum(lst)
print("Total sum =",total)