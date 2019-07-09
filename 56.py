num1,val1=map(int,input().split())
number1=list(map(int,input().split()))
countval1=0
for i in number1:
  ans1=86400-i
  res1=val1-ans1
  countval1+=1
  if res1<=0:
    break  
print(countval1)
