# Fraud Detection Using Synthetic Transaction Data

## Approach Overview
[cite_start]This project implements an end-to-end machine learning system to identify potentially fraudulent digital transactions[cite: 4]. [cite_start]Since raw transaction logs lack the historical context needed to catch smart fraudsters, the approach focuses heavily on feature engineering—translating raw timestamps and amounts into behavioral time-windows (like 24-hour transaction counts) to give the model a deeper understanding of user habits[cite: 48, 50].

## Fraud Patterns Injected
[cite_start]To ensure the synthetic data mimicked realistic, detectable fraud[cite: 36, 38], the following patterns were introduced into the dataset:
1. [cite_start]**Sudden Amount Spikes:** Fraudsters often make massive purchases quickly after compromising an account[cite: 40]. This was simulated by injecting transactions with abnormally high amounts compared to the user's baseline.
2. [cite_start]**Location Inconsistencies & Unrecognized Devices:** Fraudsters frequently operate from different cities using new devices[cite: 41]. This was simulated by generating transactions where the location deviated from the user's home city and utilized a previously unseen device ID.

## Model Choice Rationale
[cite_start]For the detection engine, **XGBoost (Extreme Gradient Boosting)** was selected[cite: 57]. 
* [cite_start]**Handling Imbalance:** Fraud is exceptionally rare[cite: 14]. XGBoost handles this well via the `scale_pos_weight` parameter, which mathematically forces the model to pay closer attention to the minority (fraud) class.
* **Non-linear Relationships:** XGBoost excels at finding complex, non-linear patterns in tabular data without requiring extensive scaling of the features.
* [cite_start]**Explainability:** It provides built-in feature importance scores, allowing us to easily answer *why* a transaction was flagged[cite: 77, 79, 83, 84].

## Evaluation Results
[cite_start]Because fraud detection is a highly imbalanced problem, accuracy alone is misleading[cite: 65]. [cite_start]The model was evaluated on the following metrics[cite: 66]:
* [cite_start]**Precision:** [1.00] [cite: 67]
* [cite_start]**Recall:** [1.00] [cite: 68]
* [cite_start]**F1-Score:** [1.00] [cite: 69]
* [cite_start]**ROC-AUC:** [1.0000] [cite: 70]

[cite_start]**Metric Trade-offs & Threshold Selection:** By default, a probability threshold of 0.5 is used for classification[cite: 73, 74]. [cite_start]However, because missing a fraudulent transaction is much more costly than a false alarm, in a real-world scenario we would likely lower this threshold (e.g., to 0.3 or 0.4)[cite: 14, 74]. [cite_start]This trade-off decreases our Precision (more false positives) but increases our Recall (catching more actual fraud), which aligns with the business goal of minimizing financial loss.

[cite_start]**Key Findings:** The feature importance analysis revealed that `amount_to_avg_ratio` and `time_since_last_txn` were the strongest predictors of fraud, confirming that behavioral deviations are more telling than isolated transaction details[cite: 52, 102].

## Assumptions Made
[cite_start]While generating the synthetic data and building the model, the following assumptions were made:
* **Location:** We assume a user's `home_location` remains mostly static for normal daily transactions, making sudden location changes a valid signal for potential fraud.
* **Data Completeness:** We assume that device IDs and locations are reliably captured by the payment gateway without null values or spoofing.
* **Time Ordering:** We assume transactions arrive at the model sequentially, allowing rolling window features to be calculated accurately in real-time.

## Part 7: Lightweight System Design
[cite_start]If this model were deployed in a production environment[cite: 87]:
* [cite_start]**Batch vs. Real-Time Detection:** The system would ideally use **real-time detection** at the point of checkout[cite: 88]. When a user swipes a card, the transaction data would be sent to an API endpoint hosting the XGBoost model. The model would calculate the rolling features on the fly and return a fraud probability score within milliseconds. [cite_start]**Batch detection** could be used as a secondary nightly sweep to catch slower, complex fraud rings[cite: 88].
* [cite_start]**Handling False Positives:** A false positive (declining a legitimate user's transaction) creates terrible user friction[cite: 89]. Instead of outright blocking a flagged transaction, the system would introduce "step-up authentication." [cite_start]The user would receive an SMS OTP (One-Time Password) or a push notification to their primary device asking, *"Did you make this purchase?"*[cite: 89].

## Limitations & Future Improvements
* [cite_start]**Limitations:** The synthetic data, while logically structured, lacks the true noise and unpredictable edge-cases found in real human behavior[cite: 103].
* [cite_start]**Future Improvements:** Implementing Graph-based approaches (like NetworkX) to map out shared devices across multiple accounts could help identify coordinated fraud rings[cite: 60, 104, 111].