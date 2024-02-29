import pandas as pd

data = {
    'empno': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'experience_years': [4, 2, 6, 11, 8, 9, 20, 15, 12, 1],
    'yearly_salary': [8, 6, 10, 15, 12, 13, 25, 18, 16, 4]
}

df = pd.DataFrame(data)
print(df)
import matplotlib.pyplot as plt
# Assuming df is the DataFrame created in step 1
plt.scatter(df['experience_years'], df['yearly_salary'])
plt.xlabel('Experience Years')
plt.ylabel('Yearly Salary')
plt.title('Scatter Plot of Experience Years vs. Yearly Salary')
plt.show()
from sklearn.linear_model import LinearRegression

# Assuming df is the DataFrame created in step 1
X = df[['experience_years']]
y = df['yearly_salary']

model = LinearRegression()
model.fit(X, y)

# To make predictions, you can use model.predict(new_data)
