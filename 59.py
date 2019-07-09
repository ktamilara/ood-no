b1,s1=map(str,input().split("|"))
c1=input()
if  len(b1)>len(s1):
    if len(b1)==len(s1)+len(c1):
        print(b1+"|"+s1+c1)
elif len(b1)<len(s1):
     if len(s1)==len(b1)+len(c1):
        print(b1+c1+"|"+s1)
elif len(b1)==len(s1) and len(c)>1 or (len(s1) or len(b1)):
    print("impossible")
