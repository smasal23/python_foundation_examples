# Write a program to rotate the given string by the given number of times.
S, K = input().split()
K = int(K)

K = K % len(S)

rotate = S[-K:] + S[:-K]

print(rotate)