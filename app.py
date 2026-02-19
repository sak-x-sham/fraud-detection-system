import streamlit as st
import pandas as pd
import xgboost as xgb
import time

# --- Page Configuration ---
st.set_page_config(page_title="Fraud Detection API", page_icon="💳")

# --- Load Model and Data ---
@st.cache_resource
def load_model():
    model = xgb.XGBClassifier()
    model.load_model('fraud_model.json')
    return model

@st.cache_data
def load_data():
    # Load the engineered data
    df = pd.read_csv('engineered_transactions.csv')
    return df

model = load_model()
df = load_data()

# --- UI Layout ---
st.title("💳 Real-Time Fraud Detection System")
st.write("This dashboard simulates a live payment gateway. Enter a transaction row number below to run it through the XGBoost model.")
st.markdown("---")

# --- Manual Selection ---
# Create a number input for the user to select a specific row (from 0 to the length of the dataset)
max_row = len(df) - 1
selected_index = st.number_input(f"Enter Transaction Row Number (0 to {max_row}):", min_value=0, max_value=max_row, value=0)

# --- Simulation Button ---
if st.button("🔍 Analyze Transaction", type="primary"):
    with st.spinner('Processing transaction...'):
        time.sleep(0.5) # Add a small delay to simulate network latency
        
        # Pull the specific transaction the user selected
        transaction_data = df.iloc[[selected_index]].copy()
        
        # Extract the actual label and drop it from the features
        actual_label = transaction_data['is_fraud'].values[0]
        features = transaction_data.drop(columns=['is_fraud'])
        
        # Make Prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] * 100
        
        # --- Display Results ---
        st.subheader(f"Details for Transaction #{selected_index}:")
        
        # Display key metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Transaction Amount", f"${features['amount'].values[0]:.2f}")
        col2.metric("Txns in Last 24h", int(features['txns_last_24h'].values[0]))
        col3.metric("Amount to 24h Avg Ratio", f"{features['amount_to_avg_ratio'].values[0]:.2f}x")
        
        # Show actual status for context
        actual_status = "Fraud" if actual_label == 1 else "Normal"
        st.write(f"**Actual Status in Database:** {actual_status}")
        
        st.markdown("---")
        st.subheader("Model Decision:")
        
        if prediction == 1:
            st.error(f"🚨 **FRAUD DETECTED** (Confidence: {probability:.2f}%)")
            st.write("Action: Transaction Blocked. Step-up authentication required.")
        else:
            st.success(f"✅ **TRANSACTION APPROVED** (Fraud Probability: {probability:.2f}%)")
            st.write("Action: Processed successfully.")