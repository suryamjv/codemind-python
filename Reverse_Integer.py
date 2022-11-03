n=int(input())
def reverse(x):
    s=0
    while(x):
        i=x%10
        s=s*10+i
        x=x//10
    return s
if n < 0:
    t = -n
else:
    t = n
x = reverse(t)
if n < 0:
    print(-x)
else:
    print(x)
    