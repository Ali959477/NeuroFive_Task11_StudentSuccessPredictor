# Case Study — Student Success Predictor

## The Challenge
Student performance is influenced by a combination of study behavior, attendance, previous academic results, learning environment, and support systems. The challenge was to build a practical machine-learning product rather than a standalone notebook.

## The Approach
The project starts with a dataset of 6,607 student records. Data quality checks were performed before handling missing values through a reproducible preprocessing pipeline. Exploratory analysis was used to understand relationships among attendance, study behavior, previous scores, and the target exam score. Three engineered indicators were added to capture study-attendance interaction, academic consistency, and study-sleep interaction.

Five regression algorithms were trained and evaluated using MAE, RMSE, and R². Ridge Regression achieved the strongest held-out performance, with an R² of 0.770 and MAE of 0.454. The final model was serialized and integrated into a Streamlit application.

## Real-World Value
The deployed application gives educators or students a quick estimate of expected exam performance from observable learning factors. It can support conversations about study planning, attendance, and academic support. The model is intended as decision support rather than an automated grading system.

## What I Learned
This capstone strengthened the complete ML lifecycle: translating a real problem into a measurable target, preparing mixed-type data, engineering useful features, comparing multiple models, selecting a model based on objective metrics, packaging the pipeline, and deploying it as an interactive product.
