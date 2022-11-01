n=int(input())
l=list(map(int,input().split()))
#print(l)
for i in range(len(l)-1,-1,-1):
    #print(i,end=" ")
    if l[i]%2==0:
        print(i,end=" ")
        break

