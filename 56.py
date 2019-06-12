q=input()
r=0
s=0
for i in q:
    if(i.isalpha()==True):
        r=1
    elif(i.isdigit()==True):
        s=1
if(r==1 and s==1):
    print("Yes")
else:
    print("No")
