word = input()
i = 0
for _ in range(0, len(word), 10):
    print(word[i : i + 10])
    i = i + 10