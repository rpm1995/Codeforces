n = int(input())

for _ in range(n):

    t = int(input())
    inputs = []

    for _ in range(t):
        inputs.append(list(map(int, input().split())))
    valid = True

    for i in range(1, t):

        if t == 1:
            break

        prev_play = inputs[i-1][0]
        prev_clear = inputs[i-1][1]
        cur_play = inputs[i][0]
        cur_clear = inputs[i][1]
        diff_play = cur_play - prev_play
        diff_clear = cur_clear - prev_clear

        if diff_play < 0 or diff_clear < 0:
            valid = False
            break

        elif diff_play == 0 and diff_clear > 0:
            valid = False
            break

        elif diff_clear > diff_play:
            valid = False
            break

    print("YES") if valid else print("NO")
