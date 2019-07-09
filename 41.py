aa1,abh=input().split()
aa1=int(aa1)
abh=int(abh)
as=''
au=2
if(aa1+abh<=3):
    for i in range(0,aa1+abh):
        if(i%2!=0):
            as=as+'0'
        else:
            as=as+'1'
else:    
    for i in range(0,aa1a+bh):
        if(i==au):
            as=as+'0'
            if(au==abh):
                au=au+2
            else:
                au=au+3
        else:
            as=as+'1'
ax=len(as)-1
if(int(as[ax])==0):
    print('-1')
elif aa1==1 and abh==2: print("011")
else:
    print(as)
