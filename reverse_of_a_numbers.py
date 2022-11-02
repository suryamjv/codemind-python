def revers(x):
    s=0
    while(x>0):
        l=x%10
        s=s*10+l
        x=x//10
    return(s)
n=int(input())
print(revers(n))