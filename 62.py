n=input()
x=0
for i in n:
    if ((i=='0') or (i=='1')):
        x+=1
if(x==len(n)):
    print("yes")
else:
    print("no")
