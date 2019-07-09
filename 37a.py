nin1=int(input())
sll1=[int(i) for i in input().split()]
sc1=0
for i in range(1,nin1-1):
    if sll1[i]<sll1[i-1] and sll1[i]<sll1[i+1]:
        sc1+=1
    elif sll1[i]>sll1[i-1] and sll1[i]>sll1[i+1]:
        sc1+=1
print(sc1)
