# 예상 시간복잡도: O(N)
def solution(my_string):
    tmp = ''.join([i if i.isdigit() else '.' for i in my_string ]).replace('.', ' ').split()
    return sum(map(int,tmp))
