# 숫자찍기

def printNumber(n):
    if n==0:
        return print("출력이 끝")
    print(n)
    printNumber(n-1)

printNumber(10)