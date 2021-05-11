# Contest MAY21C
# Question LKDNGOLF

t = int(input())
for i in range(t):
    list_of_input = list(map(int, input().split()))
    list_of_input[0]=list_of_input[0]+1
    if list_of_input[1]%list_of_input[2] == 0:
        print("Yes")
    elif (list_of_input[0]-list_of_input[1]) % list_of_input[2] ==0:
        print("YES")
    else:
        print("NO")