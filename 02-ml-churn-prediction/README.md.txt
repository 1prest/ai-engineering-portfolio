# Customer Churn Prediction (Machine Learning Project)

This project builds a machine learning model to predict customer churn. Churn refers to customers who stop using a company's services. Companies use churn prediction to improve customer retention strategy.

## 🧠 Goal
Predict whether a customer is likely to leave the service based on:
- Account balance
- Age
- Tenure
- Number of products
- Credit card usage
- Activity status
- Estimated salary

## 📊 Dataset
- 800 customer records
- Numeric and categorical features
- Target variable: `Churn` (0 = Stayed, 1 = Left)

## 🔧 Technologies Used
| Tool | Purpose |
|------|---------|
| Python | Programming |
| Pandas | Data analysis |
| Scikit-Learn | ML model |
| RandomForestClassifier | Prediction model |
| Jupyter Notebook | Workflow execution |

## ✅ Model Performance
Model Accuracy: **0.9625**

## 🔍 Key Insights

| Feature | Interpretation |
|--------|----------------|
| IsActiveMember | Inactive customers are far more likely to churn. Engagement matters. |
| Balance | Customers with lower balances show higher churn risk. |
| NumProducts | Customers using only one product churn more. |
| Tenure | New customers (<12 months) are more likely to churn. |
| Age | Churn increases slightly with age. |

### 🧩 Business Takeaways
1. Improve **customer engagement** → reduces churn.
2. Encourage **multi-product adoption** → increases loyalty.
3. Focus on **new customer onboarding** → retention opportunity.
4. Offer **value messaging to low-balance customers**.

## 📦 Files
| File | Description |
|------|-------------|
| `churn_model.ipynb` | Full notebook workflow |
| `data/churn_data.csv` | Dataset |
| `churn_model.pkl` | Saved ML model ready for deployment |
