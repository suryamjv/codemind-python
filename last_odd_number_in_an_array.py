n=int(input())
l=list(map(int,input().split()))
for i in l[::-1]:
    if i%2!=0:
        print(i,end=" ")
        break
