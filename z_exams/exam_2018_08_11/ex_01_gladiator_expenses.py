lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_expenses = (lost_fights // 2) * helmet_price
sword_expenses = (lost_fights // 3) * sword_price
shield_expenses = (lost_fights // 6) * shield_price
armor_expenses = (lost_fights // 12) * armor_price

total = helmet_expenses + sword_expenses + shield_expenses + armor_expenses
print(f"Gladiator expenses: {total:.2f} aureus")
