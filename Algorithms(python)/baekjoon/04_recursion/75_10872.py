n=int(input())

def factorial(n):
    result=1    # 0팩토리얼=1ㄴ

    if n>0:
        result=n*factorial(n-1)
    return result

print(factorial(n))

'''
n=int(input())
result=1

if n>0:
    for i in range(1,n+1):
        result*=i

print(result)

'''
