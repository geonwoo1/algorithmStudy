# n번째 피보나치수열 구하기

# 0 1 1 2 3 5 8 .....

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-2)+fibo(n-1)


print(fibo(7))
