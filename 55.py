nnum1,knum1 = map(int,input().split())
u1 = list(map(int,input().split()))
v1,w1 = 0,[]
for i in range(0,len(u1)):
  t1 = i
  for a in range(0,len(u1)):
    for l in range(0,knum1):
      if l == knum1-1:
        try:
          v1 += u1[a1+i]
        except IndexError:
            t1 = t1-1
            v1 +=u1[t1]
      else:
        v 1+= u1[i]
    w1.append(v1)
    v1 = 0
for i in range(0,len(u1),knum1):
  v1 = sum(u1[i:i+knum1])
  w1.append(v1)
print(*sorted(set(w1)))
