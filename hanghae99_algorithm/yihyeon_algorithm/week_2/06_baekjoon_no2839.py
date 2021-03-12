# 백준 2839번 (설탕 배달)

kg = int(input())   # 배달해야 하는 무게
bag = 0             # 몇 봉지 가져가면 되는지, 봉지 수

# kg = 21kg
# 21 = 5*4 + 1 / 3*7 + 0
#      5*3 + 6 -> 5*3 + 3*2  = min(5), 15 + 6
# kg = 21kg -> 21 -3 = 18kg, 18 -3 = 15kg   # 7kg -> 4kg, 1kg, -2kg
while True:
    if kg % 5 == 0:
        bag = bag + (kg // 5)
        print(bag)
        break

    kg = kg - 3
    bag = bag + 1

    if kg < 0:
        print(-1)
        break