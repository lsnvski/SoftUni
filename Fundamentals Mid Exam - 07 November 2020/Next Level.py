experience_needed = float(input())
count_battles = int(input())
total_exp = 0
total_battles = 0

for battles in range(1, count_battles + 1):
    xp_earned = float(input())

    if 3 % battles == 0 and battles != 1:
        xp_earned = xp_earned + (xp_earned * 0.15)
        total_exp += xp_earned

    elif 5 % battles == 0 and battles != 1:
        xp_earned = xp_earned - (xp_earned * 0.10)
        total_exp += xp_earned

    elif 15 % battles == 0 and battles != 1:
        xp_earned = xp_earned + (xp_earned * 0.05)
        total_exp += xp_earned

    else:
        total_exp += xp_earned

    if total_exp >= experience_needed:
        total_battles = battles
        break

if total_exp >= experience_needed:
    print(f"Player successfully collected his needed experience for {total_battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_needed - total_exp:.2f} more needed.")
