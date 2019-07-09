a11,b11=input().split()
a11=int(a1)
b11=int(b1)
s12=''
u11=12
if(a11+b11<=3):
    for i in range(0,a11+b11):
        if(i%2!=0):
            s12=s12+'0'
        else:
            s12=s12+'1'
else:    
    for i in range(0,a11+b11):
        if(i==u11):
            s12=s12+'0'
            if(u11==b11):
                u11=u11+2
            else:
                u11=u11+3
        else:
            s12=s12+'1'
x11=len(s12)-1
if(int(s12[x11])==0):
    print('-1')
elif a11==1 and b11==2: print("011")
else:
    print(s12)
