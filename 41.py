aa1,ab1=input().split()
aa1=int(aa1)
ab1=int(ab1)
as1=''
au1=2
if(aa1a+b1<=3):
    for i in range(0,aa1+ab1):
        if(i%2!=0):
            as1=as1+'0'
        else:
            as1=as1+'1'
else:    
    for i in range(0,aa1a+b1):
        if(i==au1):
            as1=as1+'0'
            if(au1==ab1):
                au1=au1+2
            else:
                au1=au1+3
        else:
            as1=as1+'1'
ax1=len(as1)-1
if(int(as1[ax1])==0):
    print('-1')
elif aa1==1 anda b1==2: print("011")
else:
    print(as1)
