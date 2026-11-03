import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# 1. Load the balanced CSV
print("Loading balanced_customer_reviews.csv...")
df = pd.read_csv("balanced_customer_reviews.csv")

# 2. Map text labels to numbers
label_map = {"negative": 0, "neutral": 1, "positive": 2}
df['label_num'] = df['sentiment'].map(label_map)

# 3. Train/Test Split (Using 'review' as the text column)
X_train, X_test, y_train, y_test = train_test_split(
    df['review'], df['label_num'], test_size=0.2, random_state=42
)

# 4. Build the Pipeline (Removed multi_class argument)
model = Pipeline([
    ('tfidf', TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=30000,
        stop_words='english',
        sublinear_tf=True,
        min_df=2
    )),
    # scikit-learn now handles 3+ classes automatically
    ('clf', LogisticRegression(max_iter=2000))
])

# 5. Train
print("\nTraining the 3-Class Model...")
model.fit(X_train, y_train)

# 6. Evaluate
test_predictions = model.predict(X_test)

print("\n--- FINAL 3-CLASS RESULTS (BALANCED DATASET) ---")
print(f"Test Accuracy: {accuracy_score(y_test, test_predictions) * 100:.2f}%")

print("\nClassification Report (Test Set):")
print(classification_report(y_test, test_predictions, target_names=["Negative", "Neutral", "Positive"]))