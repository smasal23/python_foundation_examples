# Given a string as input, you have to reverse the string by keeping the punctuation and spaces intact. You have to modify
# the source string itself without creating another string.

N = list(input())  # Take the input as a list

i, j = 0, len(N) - 1  # Initialize two pointers - i → starts from the left; j → starts from the right

while i < j:            # Loop continues as long as left pointer is before right pointer; Once they cross, reversing is done
    if not N[i].isalnum():  # Skip punctuation on the left
        i += 1
    elif not N[j].isalnum():  # Skip punctuation on the right
        j -= 1
    else:                  # Swap letters and numbers
        N[i], N[j] = N[j], N[i]
        i += 1
        j -= 1

print("".join(N))