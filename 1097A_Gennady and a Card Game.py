table = input()
hand = list(input().split())

table_rank = table[0]
table_suit = table[1]
found = False

for cur in hand:
    if cur[0] == table_rank or cur[1] == table_suit:
        found = True
        break

print("YES") if found else print("NO")
