from collections import deque

n = int(input())

card = deque()
for i in range(n):
    card.append(i+1)
# print(card)

i = 1
while(len(card)>1):
    if i == 1:
        card.popleft()
        i = 2
    else:
        card.append(card.popleft())
        i = 1
print(card[0])
