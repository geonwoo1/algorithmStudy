# 하노이

def hano(n):
    if n==1:
        return 1
    return hano(n-1)+hano(1)+hano(n-1)

print(hano(2))