def is_prime(num):
    if num<2:return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:return False
    return True
lst=[]
n=int(input())
t = n
while(n>0):
    l=n%10
    lst.append(l)
    n=n//10
cnt = 0
for i in lst:
    if(is_prime(i)==True):
        cnt += 1
if len(lst) == cnt and is_prime(t):
    print('Mega Prime')
else:
    print('Not Mega Prime')