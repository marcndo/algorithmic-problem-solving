"190. Reverse Bits"

def reverse_bit(n):
    bin_repr = list(bin(n)[2:])
    i, j = 0, len(bin_repr) - 1
    print(bin_repr)
    while i < j:
        bin_repr[i], bin_repr[j] = bin_repr[j], bin_repr[i]
        i += 1
        j -= 1
    result = 0
    length = len(bin_repr)
    for i in range(length):
        result += int(bin_repr[i]) * 2 ** (length - (i+1))
    return result

print(reverse_bit(10))
