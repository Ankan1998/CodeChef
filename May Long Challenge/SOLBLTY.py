# Contest MAY21C
# Question SOLBLTY

t = int(input())
for i in range(t):
    list_of_input = list(map(int, input().split()))
    g_ml = list_of_input[1] + (100 - list_of_input[0])*list_of_input[2]
    print(g_ml*10)