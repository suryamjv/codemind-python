a=int(input()) # 38
def repeat(num):
    s=0
    while(num>0):
        l=num%10
        s+=l
        num=num//10
    return s 
while a > 9:
    a = repeat(a) 
print(a)