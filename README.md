# Titanic Survival Prediction 🚢

## 📌 Task 11 — Titanic Survival Prediction

A machine learning project that predicts whether a Titanic passenger would survive based on passenger information such as passenger class, gender, age, fare, family members, and port of embarkation.

The trained machine learning model is integrated with a Streamlit web application to provide an easy-to-use prediction interface.

---

## 🎯 Problem Statement

The objective of this project is to build a machine learning model that can predict the survival status of Titanic passengers.

Given passenger details, the model predicts:

- **Survived (1)** — Passenger is predicted to survive
- **Not Survived (0)** — Passenger is predicted not to survive

The project demonstrates data preprocessing, feature engineering, machine learning model training, model serialization, and deployment through Streamlit.

---

## 🛠️ Approach

The project follows these main steps:

### 1. Data Preparation

- Loaded the Titanic dataset using Pandas.
- Selected relevant passenger features.
- Handled missing values using imputation.
- Separated numerical and categorical features.

### 2. Features Used

The model uses the following features:

- `Pclass` — Passenger class
- `Sex` — Passenger gender
- `Age` — Passenger age
- `SibSp` — Number of siblings/spouses aboard
- `Parch` — Number of parents/children aboard
- `Fare` — Ticket fare
- `Embarked` — Port of embarkation

### 3. Preprocessing

A Scikit-learn pipeline was created to automatically preprocess the input data.

- Numerical features are handled using imputation and scaling.
- Categorical features are handled using imputation and One-Hot Encoding.

### 4. Machine Learning Model

A **Random Forest Classifier** was trained to predict passenger survival.

The complete preprocessing and model pipeline was saved as:

`model.pkl`

---

## 🌐 Live Demo

🚀 **Try the Titanic Survival Prediction App:**

[**Titanic Survival Prediction — Live Demo**](https://titanic-prediction-task-11.streamlit.app/)

The application allows users to enter passenger details and get an instant Titanic survival prediction.

---

## 📊 Results

The trained Random Forest model successfully predicts Titanic passenger survival based on the provided passenger information.

The Streamlit application provides:

- Passenger information input
- Instant survival prediction
- Clear prediction result
- Easy-to-use interactive interface

---

## 💻 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Ali959477/NeuroFive_Task11_StudentSuccessPredictor/tree/main
