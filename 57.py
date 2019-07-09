aa1,bb1=map(str,input().split())
count1=0
for i in range(0,len(aa1)):
    for j in range(0,len(bb1)):
        if aa[i]==bb1[j]:
            coun1t+=1
if count1>=2:
    print("yes")
else:
    print("no")
