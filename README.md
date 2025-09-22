# Titanic Dataset: Data Cleaning & Preprocessing

This project demonstrates **data cleaning and preprocessing** for the Titanic dataset using Python, Pandas, NumPy, Matplotlib/Seaborn, and scikit-learn. The goal is to prepare the dataset for machine learning tasks.

---

## 📂 Project Structure

data-prep-project/
│
├─ data/
│ └─ titanic.csv # Raw dataset
│
├─ scripts/
│ ├─ test_load.py # Test dataset load & info check
│ ├─ data_cleaning.py # Handle missing values, encode categorical, scale numerical
│ └─ full_data_preprocessing.py # Complete preprocessing workflow + outlier removal
│
├─ notebooks/
│ └─ data_prep.ipynb # Optional interactive Jupyter notebook
│
├─ outputs/
│ └─ processed_titanic.csv # Cleaned & preprocessed dataset
│
└─ venv/ # Python virtual environment (ignored in Git)

---

## ✅ Features Implemented

1. **Load dataset & explore basic info**  
2. **Handle missing values** (`Age`, `Embarked`, drop `Cabin`)  
3. **Convert categorical variables to numerical** (`Sex`, `Embarked`)  
4. **Standardize numerical features** (`Age`, `Fare`)  
5. **Visualize & remove outliers** using IQR method  
6. **Optional feature**: `FamilySize = SibSp + Parch + 1`  
7. **Save final cleaned dataset** (`outputs/processed_titanic.csv`)

---

## 🛠 Tools & Libraries

- Python 3.x  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- scikit-learn  

---

## ⚡ How to Run

1. Clone this repository:

```bash
git clone https://github.com/<username>/data-prep-project.git
cd data-prep-project
Create virtual environment & install dependencies:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
Run full preprocessing script:

```bash
python scripts/full_data_preprocessing.py
Check cleaned dataset:

```bash
outputs/processed_titanic.csv
💡 Notes
Virtual environment (venv/) is ignored in GitHub.

Use requirements.txt to recreate the environment.

This dataset is ready for machine learning model training.

📈 Next Steps
Train/test split for ML

Build simple models (Logistic Regression, Decision Tree, etc.)

Exploratory Data Analysis (EDA) and feature selection

yaml
Copy code
