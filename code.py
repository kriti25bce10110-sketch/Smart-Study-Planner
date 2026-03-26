# Smart Study Planner using AI + ML

from sklearn.linear_model import LinearRegression

# Step 1: Dataset (past study data)
# [Difficulty, Study Hours]
X = [[1, 1],[2, 2],[3, 2.5],[4, 3],[5, 4]]

# Time taken to complete (output)
y = [1, 2, 3, 5, 7]

# Step 2: Create ML model
model = LinearRegression()

# Step 3: Train the model (Machine Learning happens here)
model.fit(X, y)

# Step 4: Take user input
difficulty = int(input("Enter subject difficulty (1-5): "))
hours = float(input("Enter study hours: "))

# Step 5: Predict time using ML
predicted_time = model.predict([[difficulty, hours]])

# Step 6: AI-based decision (simple logic)
print("Predicted Completion Time:", round(predicted_time[0], 2), "hours")

if predicted_time[0] <= 2:
    print("Easy subject, you can finish quickly!")
elif predicted_time[0] <= 5:
    print("Moderate subject, plan properly.")
else:
    print("Difficult subject, give more time!") 
