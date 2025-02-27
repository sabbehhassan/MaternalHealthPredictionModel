import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("backend/data/maternal_health.csv")


# Split into Features (X) and Target (y)
X = df.drop(columns=['RiskLevel'])  # Independent Variables
y = df['RiskLevel']  # Target Variable

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save Model
with open("backend/models/maternal_health_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model Trained and Saved Successfully!")
