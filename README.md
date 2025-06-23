# Maruti Stock Analysis & Volatility Detection Dashboards

This repository hosts two **independent Streamlit applications** built to analyze historical stock data of **Maruti Suzuki**. Each app serves a distinct purpose and uses the same CSV dataset (`Maruti.csv`) for analysis.

#### 1. Stock Visualization Dashboard - https://maruti-stock-visualization.streamlit.app/
#### 2. Volatility Alert System - https://maruti-volatility-alert.streamlit.app/

---

## 📊 Stock Visualization Dashboard 

### 🎯 Purpose:
An intuitive dashboard for visual exploration of Maruti stock performance through multiple financial insights.

### 🔍 Key Features:
- **Daily Price Range**: View the daily spread between High and Low prices.
- **Stock Performance Trend**: Track year-wise changes in closing prices.
- **Volume Over Time**: Analyze trading volume patterns across the year.
- **Top N Days by Closing Price**: Identify the best-performing trading days.
- **Correlation Heatmap**: Explore relationships between High, Low, and Volume.

### 🧠 How It Works:
- A sidebar allows selection of a **year** and desired **insight**.
- Each insight displays a tailored visualization or table.
- All charts update dynamically based on user input.

---

## ⚡ Volatility Alert System 

### 🎯 Purpose:
Detect and highlight days where Maruti stock experienced unusual volatility based on user-defined thresholds.

### 🔍 Key Features:
- **Customizable Threshold (%)**: Adjust sensitivity of what qualifies as volatile.
- **Volatile Days Table**: Lists days with daily % change beyond the threshold.
- **Visual Alerts**: Highlights volatile days on a time-series line chart.
- **Year Filter**: Focus analysis on a particular year.

### 🧠 How It Works:
- Calculates daily percentage change in closing prices.
- Flags days as volatile when absolute % change exceeds the selected threshold.
- Plots daily % changes and visually marks volatile days in red.

---

## 📁 Files Included

| File              | Description                                              |
|-------------------|----------------------------------------------------------|
| `stock_analysis.py` | Streamlit app for visualizing stock trends              |
| `threshold.py`      | Streamlit app for volatility detection                  |
| `Maruti.csv`        | Historical stock data of Maruti Suzuki (used by both)  |

---

## 💾 Dataset Information

- **Filename**: `Maruti.csv`
- **Format**: CSV
- **Columns Used**: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`
- **Date Format**: `YYYY-MM-DD`
- Ensure the dataset is in the same directory as the `.py` files when running the apps.

---

## 🚀 Getting Started

### 🔧 Requirements

Install required libraries using pip:

```bash
pip install streamlit pandas matplotlib seaborn numpy
