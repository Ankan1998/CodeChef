# Contest START3C
# Question TANDP

t = int(input())
for i in range(t):
    NM = list(map(int, input().split()))
    XY = list(map(int, input().split()))
    AB = list(map(int, input().split()))
    # Thief has 2 moves right and down --> thief total moves = NM[0] - XY[0] + NM[1] - XY[1] (flatten to get better idea)
    # Police has 3 moves right, down and diagonal
    # Police will move as many diagonal as possible
    # For diagonal u(along diagonal) = u+u(along x axis and y axis)
    # Police total moves =  max(NM[0]-AB[0],NM[1]-AB[1])
    thief_move = NM[0] - XY[0] + NM[1] - XY[1]
    police_move = max(NM[0]-AB[0],NM[1]-AB[1])
    if thief_move <= police_move:
        print("YES")
    else:
        print("NO")