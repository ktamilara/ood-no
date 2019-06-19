import string
def abc(string):
    s11="abcdefghijklmnopqrstuvwxyz"
    for d11 in s11:
        if d11 not in string.lower():
            return False
    return True
string=input()
if (abc(string)==True):
    print("yes")
else:
    print("no")
