nn1,kk1 = map(int,input().split())
a1 = list(map(int,input().split()))
b1,c1 = 0,[]
for i in range(0,len(a1)):
  t1 = i
  for p1 in range(0,len(a1)):
    for l1 in range(0,kk1):
      if l1 == kk1-1:
        try:
          b1 += a1[p1+i]
        except IndexError:
            t1 = t1-1
            b1 +=a1[t1]
      else:
        b1 += a1[i]
    c1.append(b1)
    b1 = 0
for i in range(0,len(a1),kk1):
  b1 = sum(a1[i:i+kk1])
  c1.append(b1)
print(*sorted(set(c1)))
