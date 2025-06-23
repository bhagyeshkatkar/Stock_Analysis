import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Custom CSS for dark, modern, and stylish layout
st.markdown(
    """
    <style>
    /* Gradient background for the main app */
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: #E0F7FA;
        font-family: 'Segoe UI', 'Arial', sans-serif;
        padding: 10px;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #1b2735, #485563);
        color: #FFFFFF;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        border-radius: 10px;
    }

    /* Sidebar title and headers */
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {
        color: #FFD700;
        text-shadow: 1px 1px 3px #000;
    }

    /* Sidebar links and hover effects */
    .css-17eq0hr a, .css-1d391kg a {
        color: #FF6347;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .css-17eq0hr a:hover, .css-1d391kg a:hover {
        color: #FFA07A;
    }

    /* Main container text */
    .block-container {
        color: #F8F8FF;
        padding: 2rem;
    }

    /* Page title and subheader styling */
    .stMarkdown h1, .stMarkdown h2 {
        color: #00CED1;
        text-shadow: 1px 1px 3px #000000;
    }

    /* Improve layout spacing */
    .main {
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the data
df = pd.read_csv("Maruti.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar UI
st.sidebar.title("🚗 Maruti Stock Analysis")
year = st.sidebar.slider("📅 Select Year", 2000, 2024, 2024)
selected_insight = st.sidebar.selectbox(
    "📊 Select Insight",
    [
        "Daily Price Range",
        "Stock Performance Trend",
        "Volume Over Time",
        "Top N Days by Closing Price",
        "Correlation Between High, Low, and Volume"
    ]
)

st.title("📈 Real-Time Maruti Stock Data Insights")

# Filter data by year
df['Year'] = df['Date'].dt.year
filtered_df = df[df['Year'] == year]

if filtered_df.empty:
    st.warning("⚠️ No data available for the selected year.")
else:
    if selected_insight == "Daily Price Range":
        st.subheader("📉 Daily Price Range (High - Low)")
        filtered_df['Daily Price Range'] = filtered_df['High'] - filtered_df['Low']

        plt.figure(figsize=(10, 6))
        plt.plot(
            filtered_df['Date'], filtered_df['Daily Price Range'],
            color='coral', marker='o', linestyle='-', linewidth=2
        )
        plt.title('Daily Price Range Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price Range')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.xticks(rotation=45)
        st.pyplot(plt)

    elif selected_insight == "Stock Performance Trend":
        st.subheader("📈 Stock Performance Trend (Closing Price)")

        plt.figure(figsize=(10, 6))
        plt.plot(
            filtered_df['Date'], filtered_df['Close'],
            color='deepskyblue', marker='o', linestyle='-', linewidth=2
        )
        plt.title('Stock Performance Trend')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.xticks(rotation=45)
        st.pyplot(plt)

    elif selected_insight == "Volume Over Time":
        st.subheader("📊 Trading Volume Over Time")

        plt.figure(figsize=(10, 6))
        plt.bar(filtered_df['Date'], filtered_df['Volume'], color='mediumslateblue')
        plt.title('Trading Volume Over Time')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.xticks(rotation=45)
        st.pyplot(plt)

    elif selected_insight == "Top N Days by Closing Price":
        st.subheader(f"🏆 Top 5 Days by Closing Price in {year}")
        top_days = filtered_df.nlargest(5, 'Close')
        st.dataframe(top_days[['Date', 'Close']])

        colors = plt.cm.cool(np.linspace(0.4, 1, len(top_days)))
        plt.figure(figsize=(10, 6))
        plt.bar(top_days['Date'].dt.strftime('%Y-%m-%d'), top_days['Close'], color=colors)
        plt.title("Top 5 Closing Prices")
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.xticks(rotation=45)
        st.pyplot(plt)

    elif selected_insight == "Correlation Between High, Low, and Volume":
        st.subheader("📌 Correlation Between High, Low, and Volume")

        correlation_matrix = filtered_df[['High', 'Low', 'Volume']].corr()
        st.write("📋 Correlation Matrix:")
        st.dataframe(correlation_matrix)

        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap")
        st.pyplot(plt)
