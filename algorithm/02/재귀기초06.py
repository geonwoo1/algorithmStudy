def str(s):
    for i in range(len(s)-1,1,-1):
        if s[i]==')':
            for j in range(i,0,-1):
                if s[j]=="(":
                    b=int(s[j-1])*s[j+1:i]
                    s=s[:j]+b+s[i+1:]
                    str(s)

    if s not in '(':
        return len(s)

print(str("1(1(1(1(1(1(1(0(1234567890))))))))"))








# 1. 뒤에서 () 찾기
# 2. () 앞에 숫자 * () 안에 숫자
# 3. 반복