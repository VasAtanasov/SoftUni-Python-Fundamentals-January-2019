import math

SERVE_USERS_LIMIT = 50
STORAGE_UNIT_SIZE = 0.5

SERVE_COST_PER_HOUR = 2
STORAGE_UNIT_PER_HOUR = 0.5
HOST_PER_MONTH = 10

DAYS_IN_MONT = 30
HOURS_IN_DAY = 24

monthly_budget = float(input())
number_of_clients = int(input())
gb_of_data = int(input())
hosts_count = int(input())
uptime_percent = float(input())

servers_needed = math.ceil(number_of_clients / SERVE_USERS_LIMIT)
storage_needed = math.ceil(gb_of_data / STORAGE_UNIT_SIZE)

hourly_cost = SERVE_COST_PER_HOUR * servers_needed + STORAGE_UNIT_PER_HOUR * storage_needed
hosts_cost = hosts_count * HOST_PER_MONTH
monthly_cost = ((hourly_cost * HOURS_IN_DAY * DAYS_IN_MONT) + hosts_cost) * (uptime_percent / 100)

if monthly_cost > monthly_budget:
    print(f"Stay Grounded! Monthly cost: ${monthly_cost:.2f} (Need ${(monthly_cost - monthly_budget):.2f} more)")
else:
    print(f"Clouds Ahoy! Monthly cost: ${monthly_cost:.2f} (${(monthly_budget - monthly_cost):.2f} leftover)")
