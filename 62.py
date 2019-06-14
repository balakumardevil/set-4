n=input()
y=0
for i in n:
    if ((i=='0') or (i=='1')):
        y+=1
if(y==len(n)):
    print("yes")
else:
    print("no")
