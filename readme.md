# 💳 Fraud Detection & Real-Time Simulation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
This project implements an end-to-end Machine Learning pipeline to detect fraudulent digital transactions. Because raw transaction logs lack the historical context needed to catch sophisticated fraudsters, this system relies heavily on **feature engineering**—translating raw timestamps and amounts into behavioral time-windows (e.g., 24-hour transaction velocity) to give the model a deep understanding of user habits.

The project includes a custom-built **Streamlit Web Application** that acts as a live payment gateway simulator, allowing users to run transactions through the model in real-time.

### 📸 Dashboard Previews
<img width="1080" height="902" alt="Screenshot 2026-02-19 233146" src="https://github.com/user-attachments/assets/4ef186fe-33ca-467e-abdc-0eae8d0d6d49" />

Fraud Detection:
<img width="991" height="901" alt="Screenshot 2026-02-19 233125" src="https://github.com/user-attachments/assets/0dac889f-4216-4385-9f76-629da3b797c9" />


## 🚀 Key Features
* **Synthetic Data Generation:** A robust Python script generating 10,000+ realistic, time-ordered transactions with imbalanced fraud rates (1-5%).
* **Pattern Injection:** Procedurally generated fraud patterns including *Sudden Amount Spikes*, *Location Inconsistencies*, and *Device Hopping*.
* **Advanced Feature Engineering:** Creation of rolling time-windows, velocity metrics, and categorical encoding to capture behavioral deviations.
* **XGBoost Classifier:** A highly tuned ML model utilizing `scale_pos_weight` to perfectly handle the severe class imbalance of fraud detection.
* **Interactive UI:** A Streamlit dashboard for real-time transaction inference and explainability.

## 📊 Evaluation & Metrics
Because fraud detection is highly imbalanced, accuracy is a misleading metric. The model was evaluated on its ability to catch fraud while minimizing false friction:
* **Primary Drivers of Fraud:** `amount_to_avg_ratio` and `time_since_last_txn`
* **Threshold Selection:** The default 0.5 probability threshold was analyzed, noting that a lower threshold (e.g., 0.3) is often preferred in production to increase Recall (catching more fraud) at the cost of slight Precision drops.

## 💻 Tech Stack
* **Data Processing:** `pandas`, `numpy`, `Faker`
* **Machine Learning:** `scikit-learn`, `xgboost`
* **Visualization:** `matplotlib`, `seaborn`
* **Web UI:** `streamlit`

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/fraud-detection-system.git](https://github.com/yourusername/fraud-detection-system.git)
   cd fraud-detection-system
