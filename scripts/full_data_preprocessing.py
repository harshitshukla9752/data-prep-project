import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 1️⃣ Load dataset
df = pd.read_csv(r"C:\Users\harsh\data-prep-project\data\titanic.csv")
print("✅ Dataset loaded")
print(df.head())
print(df.info())
print(df.isnull().sum())

# 2️⃣ Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin'])
print("\n✅ Missing values handled")

# 3️⃣ Convert categorical to numerical
df['Sex'] = df['Sex'].map({'male':1, 'female':0})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)
print("✅ Categorical variables encoded")

# 4️⃣ Standardize numerical features
scaler = StandardScaler()
df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])
print("✅ Numerical features standardized")

# 5️⃣ Visualize outliers
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
sns.boxplot(x=df['Age'])
plt.title("Boxplot of Age")
plt.subplot(1,2,2)
sns.boxplot(x=df['Fare'])
plt.title("Boxplot of Fare")
plt.show()

# 6️⃣ Remove outliers using IQR
Q1_age = df['Age'].quantile(0.25)
Q3_age = df['Age'].quantile(0.75)
IQR_age = Q3_age - Q1_age
df = df[(df['Age'] >= Q1_age - 1.5*IQR_age) & (df['Age'] <= Q3_age + 1.5*IQR_age)]

Q1_fare = df['Fare'].quantile(0.25)
Q3_fare = df['Fare'].quantile(0.75)
IQR_fare = Q3_fare - Q1_fare
df = df[(df['Fare'] >= Q1_fare - 1.5*IQR_fare) & (df['Fare'] <= Q3_fare + 1.5*IQR_fare)]
print("✅ Outliers removed")

# 7️⃣ Optional feature: FamilySize
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# 8️⃣ Save cleaned dataset
df.to_csv(r"C:\Users\harsh\data-prep-project\outputs\processed_titanic.csv", index=False)
print("✅ Final cleaned dataset saved: outputs/processed_titanic.csv")
print(df.head())

