#예상 시간 복잡도 O(n) n str length
str = input()
answer = []
for i in str:
    if i.islower():
        answer.append(i.upper())
    else:
        answer.append(i.lower())
print(''.join(answer))
