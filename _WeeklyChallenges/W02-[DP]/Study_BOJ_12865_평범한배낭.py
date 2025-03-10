'''
BOJ #12865. 평범한 배낭 (골드5)
https://www.acmicpc.net/problem/12865
유형: Dynamic Programming(DP), Knapsack 
'''
import sys
input = sys.stdin.readline

# 입력
N, K = map(int, input().split()) # N: 물품의 수, K: 버틸 수 있는 무게
items = [[0, 0]]
for _ in range(N):
    items.append(list(map(int, input().split())))

# DP
knapsack = [[0] * (K+1) for _ in range(N+1)] # DP표는 0~K+1, 0~N+1로 구성

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = items[i][0]
        value = items[i][1]

        if j >= weight: # "현재최대무게j가 해당물건무게보다 큰 경우
            # 표의 윗 셀의 값과 현재물건의V+이전물건의V값의 최댓값을 DP[i][j]에 저장
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-weight] + value)
        else: # #"현재최대무게j가 해당물건무게보다 작은 경우 (현재 물건을 담을 수 없는 경우)
            # 이전 값을 가져온다.
            knapsack[i][j] = knapsack[i-1][j]

print(knapsack[N][K])
