n11,k1 = map(int,input().split())
a11 = list(map(int,input().split()))
b1,c1 = 0,[]
for i in range(0,len(a11)):
  t1 = i1
  for p1 in range(0,len(a11)):
    for l1 in range(0,k1):
      if l1 == k1-1:
        try:
          b1 += a11[p1+i1]
        except IndexError:
            t1 = t1-1
            b1 +=a11[t1]
      else:
        b1 += a11[i1]
    c1.append(b1)
    b1 = 0
for i in range(0,len(a11),k1):
  b1 = sum(a11[i:i+k1])
  c1.append(b1)
print(*sorted(set(c1)))
