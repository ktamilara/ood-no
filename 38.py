sxs1,sys1=map(int,input().split())
sn1=list(map(int,input().split()))
sn1=sorted(sn1)
st11,i=0,0
flag=0
while i<len(sn1)-2:
  a,b,c=sn1[i:i+3]
  for j in range(0,sys1):
    a,b,c=a+1,b+1,c+1 
    if a<=5 and b<=5 and c<=5:
      flag=1
    else:
      flag=0
  if flag==1:
    st11+=1
  i+=3
  a,b,c=0,0,0
print(st11)
