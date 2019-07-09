num1,value1=map(str,input().split("|"))
tat1=input()
if  len(num1)>len(value1):
    if len(num1)==len(value1)+len(tat1):
        print(num1+"|"+value1+tat1)
elif len(num1)<len(value11):
     if len(value1)==len(num1)+len(tat1):
        print(num1+tat1+"|"+value1)
elif len(num1)==len(value1) and len(tat1)>1 or (len(value1) or len(num1)):
    print("impossible")
