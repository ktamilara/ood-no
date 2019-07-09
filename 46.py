n1 = int(input())
play = list(map(int,input().split()))
j1 = 1
miner = sum(play)
ind = 0
while(j1<n1):
    x1 = sum(play[:j1])
    y1 = sum(play[j1:])
    if(x1>y1):
        res=x1-y1
    else:
        res=y1-x1
    if(res<miner):
       miner = res
       ind = n1-j1
       t1 = j1
    j1+=1
print(t1-ind)
