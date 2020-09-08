inp = input().split()
n = int(inp[0])
d = int(inp[1])
dp = [-1 for _ in range(n)]
dp[0] = 0
s = input()

for index, current in enumerate(s):

    if current == "0" or index == 0:
        continue

    start = 0 if index - d < 0 else index - d
    min_ = float('inf')
    for step in range(start, index):
        if s[step] == "1":
            min_ = min(min_, dp[step])
    dp[index] = min_ + 1
if dp[-1] != float('inf'):
    print(dp[-1])
else:
    print("-1")
