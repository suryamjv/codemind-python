n=int(input())
l=list(map(int,input().split()))
z=int(input())
cn=0
for i in l:
    if i==z:cn+=1
print(cn)