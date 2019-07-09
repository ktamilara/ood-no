mm11=int(input())
nn11=list(map(int,input().split()))
temp=[]
while(len(nn11)!=0):
  if len(nn11)>1:
    temp.append(max(nn11))
    temp.append(min(nn11))
    nn11.remove(max(nn11))
    nn11.remove(min(nn11))
  else:
    temp.append(max(nn11))
    nn11.remove(max(nn11))
print(*temp,end="")  
