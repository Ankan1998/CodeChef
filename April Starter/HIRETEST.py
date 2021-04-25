# Contest START3C
# Question HIRETEST

t = int(input())
for i in range(t):
    NM = list(map(int,input().split()))
    XY = list(map(int, input().split()))
    passlist = []
    for j in range(NM[0]):
        #for z in range(NM[1]):
        wr = list(map(str, input().split()))
        if wr[0].count('F') >= XY[0]:
            passlist.append(1)
        elif wr[0].count('F') >= XY[0]-1  and wr[0].count('P') >=XY[1]:
            passlist.append(1)
        else:
            passlist.append(0)
    print("".join(str(x) for x in passlist))