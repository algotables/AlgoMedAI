from sklearn.linear_model import LogisticRegression
import numpy as np

# Expanded sample training data
X_train = np.array([
    [25, 3, 0], [45, 7, 1], [32, 5, 0], [60, 8, 1],
    [44, 1, 0], [55, 2, 0], [23, 4, 1], [37, 6, 1]
])

# Labels for whether a diagnosis is correct (1 = correct, 0 = incorrect)
y_train = np.array([1, 0, 1, 0, 1, 1, 0, 0])

# Initialize the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

def validate_healthcare_data(age, severity, conditions, threshold=0.4):
    """Validate healthcare data using the trained AI model with a custom threshold."""
    X_new = np.array([[age, severity, conditions]])
    probability = model.predict_proba(X_new)[0][1]  # Probability that data is valid (class 1)
    
    # If the probability is above the threshold, return True (valid), else False
    return probability >= threshold
