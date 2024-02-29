from statistics import LinearRegression
import pandas as pd

data = {
    'empno': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'experience_years': [4, 2, 6, 11, 8, 9, 20, 15, 12, 1],
    'yearly_salary': [8, 6, 10, 15, 12, 13, 25, 18, 16, 4]
}
df = pd.DataFrame(data)
X = df[['experience_years']]
y = df['yearly_salary']

model = LinearRegression(X,y)
model.fit(X,y)