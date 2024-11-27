from bisect import bisect_left
def minimum_moves_to_sort(arr):
    n = len(arr)
    lis = []
    for num in arr:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    return n - len(lis)

N = int(input())
kids = []
for _ in range(N):
    kids.append(int(input()))
print(minimum_moves_to_sort(kids))