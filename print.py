N,K=map(int,input().split())
i=0
n=1
while(n!=N and n<N):
    i+=1
    n=K**i
if(n==N):
    print("yes")
else:
    print("no")
