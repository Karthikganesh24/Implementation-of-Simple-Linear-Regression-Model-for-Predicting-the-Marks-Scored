import numpy as np
import matplotlib.pyplot as plt

# Hours studied (X) and marks scored (Y)
X = np.array([1, 2, 3, 4, 5])
Y = np.array([35, 40, 50, 60, 70])

# Calculate mean values
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Calculate slope
m = np.sum((X - mean_x) * (Y - mean_y)) / np.sum((X - mean_x) ** 2)

# Calculate intercept
b = mean_y - m * mean_x

# Regression equation
print("Slope:", round(m, 2))
print("Intercept:", round(b, 2))
print("Regression Equation: Y = {:.2f}X + {:.2f}".format(m, b))

# Predict marks for 6 hours of study
hours = 6
predicted_marks = m * hours + b

print("Hours Studied:", hours)
print("Predicted Marks:", round(predicted_marks, 2))

# Plot actual data and regression line
Y_pred = m * X + b

plt.scatter(X, Y, color="blue", label="Actual Marks")
plt.plot(X, Y_pred, color="red", label="Regression Line")

plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.title("Simple Linear Regression - Marks Prediction")
plt.legend()
plt.grid(True)
plt.show()
