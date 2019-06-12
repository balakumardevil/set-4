p1,p2=input().split()
p1=int(p1)
p2=int(p2)
c=0
temp=list(map(int,input().split()))
for a in temp:
    if(a==p2):
        c=c+1
        break
if(c!=0):
    print("yes")
else:print("no")
