import itertools
te1=input()
lii1=""
ana1 = itertools.permutations(te1,5)
for k1 in ana1: 
  lii1=''.join(k1)
if lii1 == "dhoni":
  print("yes") 
else:
  print("no")
