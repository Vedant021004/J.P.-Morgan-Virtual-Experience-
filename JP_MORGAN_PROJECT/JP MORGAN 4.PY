
import pandas as pd

# Load data
df = pd.read_csv("Task 3 and 4_Loan_Data.csv")

# Number of rating buckets
num_buckets = 10

# Create quantized buckets
df["rating"] = pd.qcut(
    df["fico_score"],
    q=num_buckets,
    labels=False
)

# Reverse ratings so lower rating = better credit score
df["rating"] = num_buckets - df["rating"]

# Display bucket boundaries
bucket_boundaries = pd.qcut(
    df["fico_score"],
    q=num_buckets,
    retbins=True,
    duplicates="drop"
)[1]

print("Bucket Boundaries:")
print(bucket_boundaries)

print("\nSample Ratings:")
print(df[["fico_score", "rating"]].head())


def fico_to_rating(fico_score, boundaries):
    """
    Convert FICO score to rating.
    Lower rating = better credit quality.
    """

    for i in range(len(boundaries) - 1):
        if boundaries[i] <= fico_score <= boundaries[i + 1]:
            return len(boundaries) - i - 1

    return None


# Example
score = 720
rating = fico_to_rating(score, bucket_boundaries)

print(f"\nFICO Score: {score}")
print(f"Rating: {rating}")



'''sed quantization to divide FICO scores into 10 buckets with approximately equal numbers of borrowers.
Each bucket is assigned a rating.
Lower ratings correspond to better credit quality.
This approach generalizes well to future datasets because bucket boundaries are derived automatically from the score distribution. '''