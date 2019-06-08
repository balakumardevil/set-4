v=int(input())
n=v
c=0
while (n!=1):
    n=n//2
    c=c+1
t=2**c
if (v==t):
    print("yes")
else:
    print("no")
