
def solution(numer1, denom1, numer2, denom2):
    answer = []
    resultnumer = (numer1 * denom2) + (numer2 * denom1)
    resultdenom = denom1 * denom2
    answer = getReducedFraction(resultnumer, resultdenom)
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

def getReducedFraction(numer,denom):
    aPrimeFactor = getPrimeFactors(numer)
    aPrimeFactorDelList = []
    bPrimeFactor = getPrimeFactors(denom)
    loop = len(aPrimeFactor)
    for i in range(0,loop):
        if aPrimeFactor[i] in bPrimeFactor:
            aPrimeFactorDelList.append(aPrimeFactor[i])
            bPrimeFactor.pop(bPrimeFactor.index(aPrimeFactor[i]))
    for i in range(0,len(aPrimeFactorDelList)):
        aPrimeFactor.pop(aPrimeFactor.index(aPrimeFactorDelList[i]))
    reducenumer = 1
    reducedenom = 1
    for i in aPrimeFactor:
        reducenumer = reducenumer * i
    for i in bPrimeFactor:
        reducedenom = reducedenom * i
    return reducenumer,reducedenom
