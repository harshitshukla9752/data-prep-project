import pandas as pd
from sklearn.preprocessing import StandardScaler

# 1️⃣ Load dataset
df = pd.read_csv(r"C:\Users\harsh\data-prep-project\data\titanic.csv")

# 2️⃣ Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin'])  # too many missing

# 3️⃣ Encode categorical variables
df['Sex'] = df['Sex'].map({'male':1, 'female':0})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# 4️⃣ Feature engineering (optional but useful)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# 5️⃣ Standardize numeric features
scaler = StandardScaler()
df[['Age','Fare']] = scaler.fit_transform(df[['Age','Fare']])

# 6️⃣ Save cleaned dataset
df.to_csv(r"C:\Users\harsh\data-prep-project\outputs\processed_titanic.csv", index=False)

print("✅ Data cleaning complete. File saved in outputs/processed_titanic.csv")
print(df.head())
