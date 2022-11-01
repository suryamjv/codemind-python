n=int(input())
l=list(map(int,input().split()))
x=int(input())
cn=0
for i in l:
    if i==x:
        cn+=1
if cn==0:print("False")
else:print("True")
