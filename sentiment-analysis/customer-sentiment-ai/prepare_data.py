import pandas as pd
from datasets import load_dataset

# 1. Load the dataset
print("Loading CRSD dataset...")
dataset = load_dataset("InfinitodeLTD/CRSD", split="train")

# Convert to a Pandas DataFrame for easy manipulation
df = dataset.to_pandas()

# 2. Clean the data (remove the rows with 'None' labels)
print(f"Original rows: {len(df)}")
df = df.dropna(subset=['sentiment'])
print(f"Rows after removing 'None': {len(df)}")

# 3. PERFECTLY BALANCE THE DATASET
# Find the size of the smallest class (neutral = 3084)
min_size = df['sentiment'].value_counts().min()
print(f"\nBalancing dataset to {min_size} reviews per class...")

# Take exactly min_size rows from each class (this keeps the 'sentiment' column!)
df_balanced = df.groupby('sentiment').sample(n=min_size, random_state=42).reset_index(drop=True)

# Shuffle the dataset so it's not ordered by class
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

# 4. Show the final distribution
print("\n--- PERFECTLY BALANCED DATA ---")
print(df_balanced['sentiment'].value_counts())
print(f"\nTotal rows in final balanced dataset: {len(df_balanced)}")

# 5. Save to a CSV file
output_filename = "balanced_customer_reviews.csv"
df_balanced.to_csv(output_filename, index=False)

print(f"\n✅ Data saved successfully to: {output_filename}")
print("ready.")