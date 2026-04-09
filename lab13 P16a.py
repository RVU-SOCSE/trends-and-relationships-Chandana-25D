#16a) Identify the trend of any variable using line chart from Matplotlib and Seaborn using line plot for 3Salary_Data.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("C:/Users/Chandana D/Downloads/3Salary_Data.csv")
plt.plot(df['YearsExperience'],df['Salary'])
plt.ylabel('YearsExperience')
plt.xlabel('Index')
plt.legend()
plt.show()
sns.lineplot(y=df['YearsExperience'],x=df['Salary'])
plt.show()
