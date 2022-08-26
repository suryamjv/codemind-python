l=[]
r=[]
n=int(input())
lst=list(map(int,input().strip().split()))[:n]
for i  in lst:
    if(i==0):l.append(i)
    else:r.append(i)
print(*(l+r))