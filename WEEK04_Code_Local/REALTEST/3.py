# https://www.acmicpc.net/problem/1202
# 보석 도둑
import heapq
import collections
import sys
read = sys.stdin.readline

jewel_N, bag_N = map(int, read().strip().split())

jewel_list = []
for _ in range(jewel_N):
    weight, price = map(int, read().strip().split())
    heapq.heappush(jewel_list, (-price, weight))

bag_list = [int(read().strip()) for _ in range(bag_N)]
heapq.heapify(bag_list)

# 보석에서는 가치가 제일 높은 애를 hip한다.
# 그다음은 가방이 작은 애부터 들어가는지 비교한다.
# 넣어지는 가방에 넣고, 다음으로 비싼 애를 또 찾아본다 이렇게?

total_price = 0

for i in range(jewel_N):
    now_jewel = heapq.heappop(jewel_list)
    now_price, now_weight = -now_jewel[0], now_jewel[1]
    bag_idx = 0
    temp = []
    while bag_list:
        now_bag = heapq.heappop(bag_list)
        if now_bag < now_weight:
            temp.append(now_bag)
            continue
        else:
            total_price += now_price
            break
    for b in temp:
        heapq.heappush(bag_list, b)

print(total_price)