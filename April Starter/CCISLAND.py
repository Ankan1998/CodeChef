# Contest START3C
# Question CCISLAND

t = int(input())
for i in range(t):
    list_of_input = list(map(int, input().split()))
    if min(list_of_input[0] // list_of_input[2], list_of_input[1] // list_of_input[3]) >= list_of_input[4]:
        print("YES")
    else:
        print("NO")