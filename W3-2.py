from collections import deque

player_gold = 150
barracks_A = deque()
barracks_B = deque()
orders = [
    {"unit": "劍士", "cost": 20},
    {"unit": "弓手", "cost": 30},
    {"unit": "騎士", "cost": 50},
    {"unit": "投石車", "cost": 40}
]

for round_num, order in enumerate(orders):
    print(f"--- 第 {round_num} 回合 ---")

    if round_num % 2 == 0:
        if len(barracks_A) > 0:
            unit = barracks_A.popleft()
            print(f"A 廠生產完成：{unit} 出列！")
        else:
            print("A 廠沒東西可做 (Underflow 防護成功)")

        if len(barracks_B) > 0:
            unit = barracks_B.popleft()
            print(f"B 廠生產完成：{unit} 出列！")
        else:
            print("B 廠沒東西可做 (Underflow 防護成功)")

    if not order:
        print("玩家本回合無動作，單純推進時間")
    else:
        unit_name = order["unit"]
        unit_cost = order["cost"]

        if len(barracks_A) >= 2 and len(barracks_B) >= 2:
            print(f"產線全滿！{unit_name} 訂單拒絕")
        elif player_gold < unit_cost:
            print("黃金不足，無法生產")
        else:
            player_gold -= unit_cost
            if len(barracks_B) < len(barracks_A):
                barracks_B.append(unit_name)
                print(f"{unit_name} 分派至 B 廠 (剩餘黃金：{player_gold})")
            else:
                barracks_A.append(unit_name)
                print(f"{unit_name} 分派至 A 廠 (剩餘黃金：{player_gold})")

    print(f"A: {list(barracks_A)} | B: {list(barracks_B)}")
    print()
