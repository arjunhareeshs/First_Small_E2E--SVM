# 🚢 Titanic Survival Prediction: Dead or Alive

This project predicts whether a passenger on the Titanic survived or not, based on their personal and travel details.

---

## 📌 Project Overview
- Cleaned and preprocessed Titanic dataset (handling missing values, encoding categorical features, scaling numerical features).
- Determined feature distributions (e.g., Age followed ~Normal, Fare was right-skewed, Family size was custom engineered).
- Added new features like **CabinDeck** and **FamilySize** to improve model performance.
- Built an **SVM Classification Model** with preprocessing pipeline.
- Developed a **Streamlit Interface** for user interaction.

---

## ⚙️ Features Used
- **Pclass** (Ticket class: 1st, 2nd, 3rd)
- **Sex** (male/female)
- **Age**
- **SibSp** (Siblings/Spouses aboard)
- **Parch** (Parents/Children aboard)
- **Fare**
- **Embarked** (Port of Embarkation: C, Q, S)
- **CabinDeck**
- **FamilySize**

---

## 🧹 Data Preprocessing
1. Missing values handled (mean imputation for Age, most frequent for Embarked).
2. Outliers in `Fare` capped using IQR method.
3. Categorical variables (`Sex`, `Embarked`, `CabinDeck`) encoded.
4. Feature scaling applied (StandardScaler).
5. Feature engineering:
   - **FamilySize** = SibSp + Parch
   - Extracted **CabinDeck** from Cabin column.

---

## 📊 Exploratory Data Analysis (EDA)
- **Age** → approximately Normal distribution.
- **Fare** → right-skewed distribution, log-transformed.
- **Embarked** → categorical with majority 'S'.
- **FamilySize** → positively skewed distribution.
- **Survival** more likely for **females, children, and 1st class passengers**.

*(Insert example plots here in actual report)*

---

## 🤖 Model
- **Algorithm**: Support Vector Machine (SVM)
- **Pipeline** includes preprocessing (encoding + scaling)
- Trained with cross-validation to avoid overfitting

---

## 🎯 Results
- Accuracy: ~80%
- Precision & Recall balanced
- Strong performance on minority classes (women/children survival)

---

## 💻 Streamlit Interface
A user-friendly web app was built using **Streamlit**:  

👉 Example Inputs:
- Pclass: 1  
- Sex: male  
- Age: 54  
- Fare: 51.86  
- Embarked: S  
- CabinDeck: E  
- FamilySize: 1  

👉 Example Output:
- **✅ Survived** OR **❌ Did not survive**

---

## 📷 Screenshots

### Data Distribution Example
![Distribution Example](images/distribution.png)

### Streamlit Interface
![App Screenshot](images/streamlit_app.png)

---

## 🚀 How to Run
1. Clone this repository  
   ```bash
   git clone https://github.com/yourusername/titanic-survival.git
   cd titanic-survival
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Run Streamlit app  
   ```bash
   streamlit run app.py
   ```

---

## 📌 Future Improvements
- Try **Random Forests, XGBoost** for comparison  
- Add **probability output** (e.g., "Survival Probability: 73%")  
- Deploy app on **Streamlit Cloud**

---

✍️ *Developed as part of Titanic ML challenge with enhanced preprocessing and visualization.*
