destination = input()
distance_in_gm = int(input())
budget = int(input())
consumption = float(input()) / 100
cost_per_liter = float(input()) * consumption

total_cost = distance_in_gm * cost_per_liter

if total_cost > budget:
    print(f"Maybe another time, need ${(total_cost - budget):.2f} more")
else:
    print(f"Off to {destination} with ${(budget - total_cost):.2f} for snacks")
