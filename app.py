import pandas as pd

# Sample candidate data
candidates = [
    {"Name": "Rahul Sharma", "Skills": 90, "Experience": 3},
    {"Name": "Priya Singh", "Skills": 85, "Experience": 2},
    {"Name": "Aman Verma", "Skills": 95, "Experience": 4},
    {"Name": "Neha Gupta", "Skills": 80, "Experience": 1},
]

# AI Score Calculation
for candidate in candidates:
    candidate["AI Score"] = candidate["Skills"] * 0.7 + candidate["Experience"] * 7.5

# Rank candidates
df = pd.DataFrame(candidates)
df = df.sort_values(by="AI Score", ascending=False)

print("Ranked Candidates:")
print(df)

# Save results
df.to_excel("ranked_candidates.xlsx", index=False)

print("Ranking saved to ranked_candidates.xlsx")
