def reverse(n):
    rev=0
    while(n>0):
        a=n%10
        rev=rev*10+a
        n=n//10
    return rev
num=int(input())
if reverse(reverse(num)**2)==(num**2):print("True")
else:print("False")
