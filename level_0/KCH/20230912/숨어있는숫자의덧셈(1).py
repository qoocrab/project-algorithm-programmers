# 예상 시간복잡도: O(N)
import re

def solution(my_string):
    numbers = list(map(int,list(re.sub(r'[^0-9]', '', my_string))))
    return sum(numbers)

# cf)
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])
