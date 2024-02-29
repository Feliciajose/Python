import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
data = {
    'empno': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'experience_years': [4, 2, 6, 11, 8, 9, 20, 15, 12, 1],
    'yearly_salary': [8, 6, 10, 15, 12, 13, 25, 18, 16, 4]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot Scatter Diagram
plt.scatter(df['experience_years'], df['yearly_salary'])
plt.xlabel('Experience Years')
plt.ylabel('Yearly Salary')
plt.title('Scatter Plot of Experience Years vs. Yearly Salary')
plt.show()

# Check for Linearity using Linear Regression
X = df[['experience_years']]
y = df['yearly_salary']

model = LinearRegression()
model.fit(X, y)

# Display the linear regression parameters
print(f'Intercept: {model.intercept_}')
print(f'Coefficient: {model.coef_[0]}')
