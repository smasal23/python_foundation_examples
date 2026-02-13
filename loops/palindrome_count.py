# Anto is learning about palindromic numbers. Her teacher gave him the task to count all palindromic numbers present in that range.
# Anto has told you about this and want your help. You design an algorithm in order to help Anto.
N = int(input())

count = 0
for i in range(1, N + 1):
    if str(i) == str(i)[::i]:
        count += 1

print(count)