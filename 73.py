n=int(input())
c,b=map(int,input().split())
for i in range(c,b+1):
    if(i==n):
         print("yes")
         break
else:
    print("no")
