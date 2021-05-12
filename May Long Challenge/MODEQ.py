# Contest MAY21C
# Question MODEQ

t = int(input())
for i in range(t):
    list_of_input = list(map(int, input().split())) # N, M
    count_pair = 0
    list_ = [1]*(list_of_input[0]+1)
    for a in range(2,list_of_input[0]+1):
        x = list_of_input[1] % a
        count_pair = count_pair + list_[x]
        for b in range(x,list_of_input[0]+1,a):
            list_[b] = list_[b]+1
    print(count_pair)

