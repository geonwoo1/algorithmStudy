# 팩토리얼

def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)

print(fac(3))


