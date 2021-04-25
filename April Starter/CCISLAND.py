# Contest START3C
# Qestion CCISLAND

t = int(input())
for i in range(t):
    lst = list(map(int,input().split()))
    if min(lst[0]//lst[2],lst[1]//lst[3]) >= lst[4]:
        print("YES")
    else:
        print("NO")