# 🎓 Student Success Predictor — End-to-End ML Capstone

An end-to-end Machine Learning project that predicts a student's expected **Exam Score** from academic, learning, family, and school-related factors.

## Problem Statement
Educational institutions need simple data-driven ways to identify factors associated with student performance. This project turns raw student information into a deployed prediction product that can provide an estimated exam score and highlight when additional academic support may be useful.

## Dataset
The supplied dataset contains **6,607 student records and 20 columns**. The target is `Exam_Score`.

## Workflow
1. Problem definition
2. Data loading and quality checks
3. Missing-value handling
4. Exploratory data analysis
5. Feature engineering
6. Categorical encoding + numerical scaling
7. Train/test split
8. Multiple regression models
9. Model evaluation
10. Best-model selection
11. Model serialization
12. Streamlit deployment

## Feature Engineering
- `Study_Attendance_Index`
- `Academic_Consistency`
- `Study_Sleep_Index`

## Models Compared
- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- Extra Trees Regressor

## Results
| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Ridge Regression | 0.454 | 1.803 | 0.770 |\n| Linear Regression | 0.453 | 1.803 | 0.770 |\n| Gradient Boosting | 0.703 | 1.903 | 0.744 |\n| Extra Trees | 0.993 | 2.098 | 0.689 |\n| Random Forest | 1.059 | 2.159 | 0.670 |\n
### Selected Model
**Ridge Regression** was selected based on the highest test R². On the held-out test set it achieved **R² = 0.770**, **MAE = 0.454**, and **RMSE = 1.803**.

## Project Structure
```text
Student_Success_Capstone/
├── data/student_performance.csv
├── notebooks/Capstone_Student_Success.ipynb
├── app.py
├── model.pkl
├── model_results.csv
├── metadata.json
├── requirements.txt
├── README.md
└── case-study.md
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment
The app can be deployed on Streamlit Community Cloud by connecting this GitHub repository and selecting `app.py` as the main file.

## Real-World Value
The product demonstrates how an ML workflow can turn student-level data into an accessible decision-support tool. Schools or educators could use predictions as one input for identifying students who may benefit from additional support.

## Limitations & Responsible Use
Predictions are estimates and should not be used as the sole basis for grading, admission, discipline, or other high-impact decisions. Student data should be handled with appropriate privacy protections.

## Technologies
Python • Pandas • NumPy • Scikit-learn • Streamlit • Joblib • Matplotlib/Seaborn
