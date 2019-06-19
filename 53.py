import string
str1=input()
str1=str1.lower()
li1=list(string.ascii_lowercase[0:26])
flag1=1
for i in li1:
  if i not in st1r:
    flag1=0
if flag1==0:
  print("no")
else:
  print("yes")
