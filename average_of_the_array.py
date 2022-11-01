n=int(input())
l=list(map(int,input().split()))
x=cn=0
for i in l:
    x+=i
a=x/n
#if a in l:print("True")
#else:print("False")
print("{:.2f}".format(a))