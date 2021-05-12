# Contest MAY21C
# Question XOREQUAL

# Use modular exponentiation

def mod_expo(x, y, p):
    res = 1  # Initialize result

    # Update x if it is more
    # than or equal to p
    x = x % p

    if (x == 0):
        return 0

    while (y > 0):

        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


t = int(input())
for i in range(t):
    inp = int(input())
    print(mod_expo(2, inp - 1, 10 ** 9 + 7))

