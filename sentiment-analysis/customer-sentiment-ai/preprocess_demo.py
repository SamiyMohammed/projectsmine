import re

def manual_preprocess(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove punctuation and special characters (keep only letters, numbers, spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # 3. Tokenization (split into words)
    tokens = text.split()
    
    # 4. Remove stopwords (a basic list for demo)
    stop_words = {"the", "was", "it", "just", "a", "of", "and", "to", "in", "is", "that"}
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # 5. Join back into a clean string
    return " ".join(filtered_tokens)

# Test it
raw_review = "The movie was NOT good!!! 😡 It was terrible, just a waste of time."
cleaned_review = manual_preprocess(raw_review)

print(f"ORIGINAL: {raw_review}")
print(f"CLEANED:  {cleaned_review}")