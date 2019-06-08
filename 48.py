A=list()
n=int(input())
for i in range(int(n)):
   k=int(input())
   A.append(int(k))
sm=sum(A)
avg=sm//n
print(sm)
print(avg)
