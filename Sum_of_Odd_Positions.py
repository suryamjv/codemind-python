n=int(input())
lst=list(map(int,input().split()))
os=0
for i in range(len(lst)):
    if i%2!=0:
        os+=lst[i]
print((os))