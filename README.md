# Credit Card Fraud Detection: Comparative Analysis of Machine Learning Models

A comprehensive, end-to-end machine learning project focusing on identifying fraudulent credit card transactions from a highly imbalanced dataset. This analysis implements preprocessing pipelines, handles severe class imbalances, and compares the performance of multiple classifiers to determine the best candidate for real-world deployment.

---

## 📌 Project Overview
Credit card fraud detection is a classic highly-imbalanced classification problem. In this dataset, fraudulent transactions represent less than **0.2%** of the overall data (492 frauds out of 284,807 transactions). 

Standard accuracy is a highly deceptive metric for imbalanced datasets (a dummy model predicting "legitimate" for everything achieves 99.82% accuracy). Instead, this project prioritizes **Recall** (to minimize missed frauds / False Negatives) and **F1-Score** (to balance security with customer satisfaction / False Positives).

---

## 🛠️ Key Methodology & Preprocessing
To build robust, generalizable classifiers, the following data preprocessing steps were implemented:

1. **Feature Scaling**: The `Amount` feature was scaled using **`RobustScaler`** (instead of standard scaling) to prevent extreme outliers from skewing model inputs.
2. **Stratified Split**: An 80/20 train-test split was used. **Stratified splitting** ensures that both the training and test sets maintain the exact same proportion of fraud cases as the original dataset.
3. **Handling Class Imbalance**: **SMOTE** (Synthetic Minority Over-sampling Technique) was applied **strictly to the training data only**. This generates synthetic fraudulent transactions, allowing the models to learn pattern boundaries without causing data leakage into the test evaluation.
