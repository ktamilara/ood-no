ans1=[3,4,33,34,43,44]
q1=[33,34,43,44]
n1=int(input())
on1=n1
while len(ans1)<=on1:
    a1=[]
    for i in range(3,5):
        for ii in q1:
            s1=str(i)+str(ii)
            s1=int(s1)
            a1.append(s1)
            ans1.append(s1)
    q1=a1.copy()
print(ans1[n1-1])
