# Assume that the given string has enough memory. Don't use any extra space(IN-PLACE)
# Input Description: Input type will be given string format
# Output Description: Print the decompose of the string
N = input()
output = []
i = 0

while i < len(N):
    char = N[i]
    counts = int(N[i + 1])
    output.append(char * counts)
    i += 2                          # move forward by 2 steps.

print(''.join(output))