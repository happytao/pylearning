def is_palindrome(n):
    L = list(str(n))
    l_0 = len(L)
    n = 0
    while n<l_0/2:
        if L[n] == L[-n-1]:
            n = n+1
            continue
        else:
            return None
    return n

output = filter(is_palindrome,range(1,1000))
print('1~1000',list(output))
