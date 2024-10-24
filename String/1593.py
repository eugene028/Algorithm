from collections import Counter

g, s = map(int, input().split())
W = input()
S = input()
count = 0

w_counter = Counter(W)

long_counter = Counter(S[:g])

if w_counter == long_counter:
    count += 1

for i in range(1, s - g + 1):
    long_counter[S[i - 1]] -= 1
    if long_counter[S[i - 1]] == 0:
        del long_counter[S[i - 1]]
    long_counter[S[i + g - 1]] += 1

    if long_counter == w_counter:
        count += 1
print(count)


