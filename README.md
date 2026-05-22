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

---

## 📊 Models Evaluated
Four distinct machine learning algorithms were built, trained, and compared:
*   **Logistic Regression**
*   **Decision Tree Classifier**
*   **Random Forest Classifier**
*   **Support Vector Machine (LinearSVC)**

---

## 📈 Performance Results & Comparative Analysis

Each model was evaluated on an unseen 20% test partition. The results are summarized below:

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :---: | :---: | :---: | :---: |
| 🔹 **Logistic Regression** | 0.9737 | 0.0569 | **0.9184** | 0.1072 |
| 🔹 **Support Vector Machine (SVM)** | 0.9771 | 0.0643 | 0.9082 | 0.1201 |
| 🔹 **Decision Tree** | 0.9971 | 0.3423 | 0.7755 | 0.4750 |
| 🏆 **Random Forest** | **0.9995** | **0.8989** | 0.8163 | **0.8556** |

### 🔍 Key Trade-offs Analyzed:
> [!NOTE]
> **Logistic Regression & SVM** achieved outstanding Recall (>90%), detecting the vast majority of frauds. However, their precision was extremely low (~6%), which would cause an unacceptable volume of false alarms and block legitimate transactions, harming the customer experience.

> [!TIP]
> **Random Forest** provided the most optimal balance. It achieved a strong Recall of **81.6%** while maintaining an outstanding Precision of **89.9%** (leading to a peak F1-Score of **0.8556**). 

---

## 🏆 Final Recommendation
**The Random Forest Classifier is strongly recommended for production deployment.** 

While Logistic Regression catches ~10% more frauds, the sheer volume of False Positives would overwhelm operational fraud analysts and frustrate customers. Random Forest reliably identifies over 80% of fraudulent activity with minimal false alerts.

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository
```bash
git clone https://github.com/ifta-faisal/Credit_Card_Fraud_Detection.git
cd Credit_Card_Fraud_Detection
```

### 2. Install Dependencies
Ensure you have Python installed, then install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn jupyter
```

### 3. Run the Jupyter Notebook
Open and run the analysis notebook:
```bash
jupyter notebook credit_card_fraud_detection.ipynb
```
*Note: The notebook has been configured to automatically load the local `creditcard.csv` file for instant, offline execution, bypassing the slow and unstable OpenML download server.*

---

## 🔮 Future Enhancements
*   **Threshold Tuning**: Optimize the decision threshold of the Random Forest model to further push Recall higher while keeping Precision in an acceptable range.
*   **Gradient Boosting**: Implement and evaluate modern boosting frameworks like XGBoost, LightGBM, or CatBoost to compare trade-offs.
