import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Stylish background
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #141E30, #243B55);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #1B1B2F;
    }
    h1, h2, h3 {
        color: #00FFFF;
        text-shadow: 1px 1px #000;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
df = pd.read_csv("Maruti.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Sidebar controls
st.sidebar.title("📊 Volatility Dashboard")
year = st.sidebar.slider("Select Year", 2000, 2024, 2024)
volatility_threshold = st.sidebar.slider("Volatility Threshold (%)", 0, 10, 3)

# Title
st.title("⚡ Volatility Alert System for Maruti Stocks")

# Filter by year
df['Year'] = df['Date'].dt.year
filtered = df[df['Year'] == year].copy()

# Calculate % change
filtered['Daily Change %'] = filtered['Close'].pct_change() * 100
filtered['Volatile'] = abs(filtered['Daily Change %']) > volatility_threshold

# Alert Section
st.subheader("🚨 Volatile Days")
volatile_days = filtered[filtered['Volatile']]
st.dataframe(volatile_days[['Date', 'Close', 'Daily Change %']].round(2))

# Plotting
st.subheader("📉 Daily % Change Over Time")
plt.figure(figsize=(10, 5))
plt.plot(filtered['Date'], filtered['Daily Change %'], label='Daily % Change', color='orange')
plt.axhline(y=volatility_threshold, color='red', linestyle='--', label='Volatility Threshold')
plt.axhline(y=-volatility_threshold, color='red', linestyle='--')
plt.fill_between(filtered['Date'], filtered['Daily Change %'], where=filtered['Volatile'], color='red', alpha=0.3)
plt.title("Daily Percentage Change")
plt.xlabel("Date")
plt.ylabel("% Change")
plt.grid(True)
plt.legend()
st.pyplot(plt)
