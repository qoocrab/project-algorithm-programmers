# 예상 시간 복잡도 O(n) n is sizes lenght

def solution(sizes):
    answer = 0
    width = 0
    height = 0
    for i in sizes:
        if i[0] < i[1]:
            i = swap(i)
        if i[0] > width:
            width = i[0]
        if i[1] > height:
            height = i[1]

    answer = width * height
    return answer


def swap(item):
    return [item[1], item[0]]
