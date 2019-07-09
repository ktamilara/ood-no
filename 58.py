n11=int(input())
li1=[]
a1=n11//2+n11
for i in range(1,n11+1):
    if i%2==0:
        li1.append(i)
for i in range(1,n11+1):
    if i%2!=0:
        li1.append(i)
for i in range(1,n11+1):
    if i%2==0:
        li1.append(i)
print(a1)
print(*li1)
