'''
BOJ #1202. 보석 도둑(골드2)
https://www.acmicpc.net/problem/1202
유형: Priority Queue, Data Structure, Greedy
'''
import sys
import heapq

input = sys.stdin.readline

# Step 1: 입력 받기
N, K = map(int, input().split())  # N: 보석 개수, K: 가방 개수
jewelry = []  # (무게, 가격)
bags = []  # 가방의 최대 무게

for _ in range(N):
    M, V = map(int, input().split())
    jewelry.append((M, V))

for _ in range(K):
    bags.append(int(input()))

# Step 2: 보석과 가방 정렬
jewelry.sort()  # 보석을 무게 기준으로 정렬
bags.sort()  # 가방을 무게 기준으로 정렬

# Step 3: 우선순위 큐 (최대 힙) 사용
max_heap = []
result = 0
idx = 0

# 가방을 하나씩 처리
for bag in bags:
    # 현재 가방이 수용할 수 있는 보석을 모두 추가 (무게 기준 정렬된 상태)
    while idx < N and jewelry[idx][0] <= bag:
        heapq.heappush(max_heap, -jewelry[idx][1])  # 최대 힙을 위해 음수 저장
        idx += 1

    # 가장 가치가 높은 보석을 선택
    if max_heap:
        result += -heapq.heappop(max_heap)

print(result)

