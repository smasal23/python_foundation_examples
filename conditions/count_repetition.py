# Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
N, K = map(int, input().split())
List_N = list(map(int, input().split()))

def repetition(K, N):
    if not K in List_N:
        return -1

    count = 0
    for i in List_N:
        if i == K:
            count += 1
    return count

print(repetition(K, N))
# or count = List_N.count(K)
#    print(count if count > 0 else -1)
