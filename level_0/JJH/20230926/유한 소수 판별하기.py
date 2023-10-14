#예상 시간 복잡도 O(n)
def solution(a, b):
    answer = 1
    aPrimeFactor = getPrimeFactors(a)
    bPrimeFactor = getPrimeFactors(b)

    for i in aPrimeFactor:
        if i in bPrimeFactor:
            bPrimeFactor.pop(bPrimeFactor.index(i))

    for m in bPrimeFactor:
        if m == 2 or m == 5:
            pass
        else:
            answer = 2
    return answer

def getPrimeFactors(n):
    primeFactor = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:  # found
                primeFactor.append(i)
                n = n // i
                break
    return primeFactor