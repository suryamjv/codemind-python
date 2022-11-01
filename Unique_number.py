n=int(input())
l=[]
ul=[]
c=0
while(n>0):
    i=n%10
    l.append(i)
    n=n//10
for i in l:
    if i not in ul:
        ul.append(i)
if len(l)!=len(ul):
    print("Not Unique Number")
else:
    print("Unique Number")
        


        