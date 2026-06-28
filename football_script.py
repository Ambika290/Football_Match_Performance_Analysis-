import pandas as pd
import random

data = []

# Player list
players = ["Ravi", "Arjun", "Rahul", "Vijay"]

for i in range(10):
    goals_scored = random.randint(0, 5)
    goals_conceded = random.randint(0, 5)

    # Result logic
    if goals_scored > goals_conceded:
        result = "Win"
    elif goals_scored < goals_conceded:
        result = "Loss"
    else:
        result = "Draw"

    # Assign random player
    player = random.choice(players)

    # Best performer logic (per match)
    if goals_scored >= 3:
        best_performer = "Star Player "
    elif goals_scored == 2:
        best_performer = "Good "
    else:
        best_performer = "Needs Improvement "

    data.append({
        "Match_ID": i + 1,
        "Goals_Scored": goals_scored,
        "Goals_Conceded": goals_conceded,
        "Result": result,
        "Player": player,
        "Best_Performer": best_performer
    })

df = pd.DataFrame(data)

# Save CSV
df.to_csv(r"C:\Users\Ambika\OneDrive\Desktop\football_data.csv", index=False)

print("Done! Best Performer added.")