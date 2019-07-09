number11,number12=map(str,input().split())
countvalue1=0
for i in range(0,len(number11)):
    for j in range(0,len(number12)):
        if number11[i]==number12[j]:
            countvalue1+=1
if countvalue1>=2:
    print("yes")
else:
    print("no")
