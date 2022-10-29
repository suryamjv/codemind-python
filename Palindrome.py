a=int(input())
def revers(a):
    rev=0
    while(a>0):
        l=a%10
        rev=rev*10+l
        a=a//10
    return rev
if(a==revers(a)):print("True")
else:print("False")
