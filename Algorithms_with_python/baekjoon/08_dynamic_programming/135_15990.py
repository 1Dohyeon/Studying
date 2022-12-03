import sys

t=int(sys.stdin.readline())
d=[[0 for i in range(3)] for i in range(100001)]

d[1]=[1,0,0]
d[2]=[0,1,0]
d[3]=[1,1,1]   # 1로 끝나는 경우 1개, 2로 끝나는 경우 1개, 3으로 끝나는 경우 1개

# 전 수는 1을 더해야 하므로 2와 3으로 끝난 경우의 수에 1을 더한 경우의수를 구하고
# 그 전 수는 2를 더해야 하므로 1과 3으로 끝난 경우의 수에 2를 더한 경우의 수를 위에 더하고
# 또 그 전 수는 3을 더해야 하므로 1과 2로 끝난 경우의 수에 3을 더한 경우의 수를 위에 더해야한다.

for i in range(4,100001): # 문제에서 100000까지라 했으므로 범위를 지정해준다.
        # 예를 들어 만약 i가 6일 때
    # 5에서 2와 3으로 끝난거에 1 더하기-->d[6]에서 1로 끝난 경우
    d[i][0]=d[i-1][1]%1000000009+d[i-1][2]%1000000009
    # 4에서 1과 3으로 끝난거에 2 더하기 -->d[6]에서 2로 끝난 경우
    d[i][1]=d[i-2][0]%1000000009+d[i-2][2]%1000000009
    # 3에서 1과 2로 끝난거에 3 더하기 -->d[6]에서 3로 끝난 경우
    d[i][2]=d[i-3][0]%1000000009+d[i-3][1]%1000000009

for i in range(t):
    num=int(sys.stdin.readline())
    print(sum(d[num])%1000000009)
