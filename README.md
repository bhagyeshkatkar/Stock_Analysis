# 📈 Maruti Stock Analysis & Volatility Detection Dashboard

This repository presents a dual-dashboard application built using **Streamlit**, offering powerful tools to explore and analyze historical stock data for **Maruti Suzuki**. It consists of two interactive Python applications:

1. **Stock Visualization Dashboard** – For visual and statistical exploration of Maruti stock performance.
2. **Volatility Alert System** – For detecting and highlighting days with unusual volatility.

The project uses real stock data (`Maruti.csv`) to deliver insights through a clean, modern UI.

---

## 📊 1. Stock Visualization Dashboard (`stock_analysis.py`)

### 🎯 Purpose:
An interactive dashboard for understanding stock behavior across multiple dimensions – price trends, volume activity, correlations, and top-performing days.

### 🔍 Key Features:
- **Daily Price Range**: Visualizes the daily spread between the High and Low prices.
- **Performance Trend**: Tracks closing prices to show trends over the selected year.
- **Volume Over Time**: Analyzes trading volume fluctuations.
- **Top N Days by Closing Price**: Lists and visualizes the best-performing days based on close prices.
- **Correlation Heatmap**: Shows statistical relationships between High, Low, and Volume.

### 🧠 How it works:
- A sidebar allows users to **select a year** and **choose an insight**.
- Each insight loads a customized plot or table relevant to the stock data.
- Data is filtered dynamically to match user input.

---

## ⚡ 2. Volatility Alert System (`threshold.py`)

### 🎯 Purpose:
Identify and visualize volatile trading days when the price movement exceeds a user-defined percentage threshold.

### 🔍 Key Features:
- **Custom Year & Threshold Selection** via sidebar.
- **Volatile Days Table**: Lists days where daily % change in closing price exceeds the selected threshold.
- **Time-Series Plot**: Highlights volatile days visually on a plot of daily price changes.
- **Dynamic Thresholding**: Users can experiment with different levels of sensitivity.

### 🧠 How it works:
- Computes **daily % change** in closing prices.
- Marks days as volatile when the change exceeds the specified threshold (positive or negative).
- Highlights those days in red on a line chart for easy detection.

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `stock_analysis.py` | Streamlit dashboard for visual stock insights |
| `threshold.py` | Streamlit app for detecting and displaying volatile stock days |
| `Maruti.csv` | Historical stock data of Maruti Suzuki used by both apps |

---

## 💾 Dataset Details

- **Source**: Historical stock data of Maruti Suzuki (CSV format)
- **Filename**: `Maruti.csv`
- **Columns Used**: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`
- **Date Format**: YYYY-MM-DD

The dataset should be placed in the same folder as the `.py` files.

---

## 🚀 Getting Started

### 🔧 Requirements

Install dependencies using pip:

```bash
pip install streamlit pandas matplotlib seaborn numpy
