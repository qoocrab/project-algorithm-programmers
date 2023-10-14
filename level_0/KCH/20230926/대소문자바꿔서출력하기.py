# 예상 시간복잡도: O(N)
str = input()
print(''.join(i.lower() if i.isupper() else i.upper() for i in str))

# cf) .swapcase()
