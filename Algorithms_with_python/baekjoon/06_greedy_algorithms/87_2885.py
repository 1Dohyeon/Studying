K=int(input())
l=1 # 초콜릿의 크기
n=0 # 쪼개야 하는 횟수

while l<K:  # 초콜릿은 상근이가 먹는 양보다 커야하므로 l이 k보다 커질 때까지 계속 2배씩 곱함.
    l*=2

size=l  # 크기는 고정된 값이므로 새로운 변수에 담아줌.

while K>0:
    if K>=l:    
        K-=l   
    else:
        l//=2   # k가 l보다 작을 경우 l을 2로 나눈 몫으로 줄여가면서ㄴ n을 1씩 늘린다.
        n+=1

print(size,n)


