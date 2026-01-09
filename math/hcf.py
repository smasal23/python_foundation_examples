# Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

A, B = map(int, input().split())

def hcf(A, B):
    factors_of_A = []
    factors_of_B = []
    common_factors = []

    if A == 0:
        return B
    elif B == 0:
        return A
    else:
        for i in range(1, A + 1):
            if A % i == 0:
                factors_of_A.append(i)
        for i in range(1, B + 1):
            if B % i == 0:
                factors_of_B.append(i)
        for i in factors_of_A:
            if i in factors_of_B:
                common_factors.append(i)
        return common_factors[-1]

print(hcf(A, B))