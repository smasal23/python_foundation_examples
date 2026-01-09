# Write a code get an integer number as input and print the odd and even digits of the number separately.
N = int(input())

def print_even_odd(N):
    Even_list = []
    Odd_list = []
    for i in str(abs(N)):
        if int(i) % 2 == 0:
            Even_list.append(i)
        else:
            Odd_list.append(i)

    even_list = sorted(Even_list)
    odd_list = sorted(Odd_list)

    return even_list, odd_list

even, odd = print_even_odd(N)

print(" ".join(even))
print(" ".join(odd))