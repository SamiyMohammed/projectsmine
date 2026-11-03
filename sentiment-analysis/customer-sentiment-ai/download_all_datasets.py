from datasets import load_dataset
from collections import Counter

def inspect_dataset(name, config=None, split="train"):
    print(f"\n{'='*50}\nLOADING: {name}\n{'='*50}")
    try:
        if config:
            ds = load_dataset(name, config, split=split)
        else:
            ds = load_dataset(name, split=split)
        
        print(f"Success! Rows: {len(ds)}")
        
        # Find the label column
        label_col = next((c for c in ['label', 'labels', 'sentiment', 'target'] if c in ds.column_names), None)
        if label_col:
            print(f"Label Distribution: {Counter([str(l) for l in ds[label_col]])}")
        else:
            print("No standard label column found.")
    except Exception as e:
        print(f"FAILED to load: {e}")

#inspect_dataset("cornell-movie-review-data/rotten_tomatoes")
inspect_dataset("InfinitodeLTD/CRSD")