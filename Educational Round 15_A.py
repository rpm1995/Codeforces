n = int(input())
arr = list(map(int, input().split()))
count = 1
ans = 1

for index in range(1, n):
    if arr[index] > arr[index-1]:
        count += 1

    else:
        count = 1

    ans = max(ans, count)

print(ans)
