size=int(input())
ls=list(map(int,input().split()))
esum=0
osum=0
for i in range(size):
    if(ls[i]%2==0):
        esum+=ls[i]
    else:
        osum+=ls[i]
print(osum,esum)