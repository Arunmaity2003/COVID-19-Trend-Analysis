# COVID-19 Trend Analysis using Data Visualization

## 📌 Overview
The COVID-19 pandemic has had a significant global impact. This project aims to analyze and visualize COVID-19 data to better understand how the virus spread over time, which regions were most affected, and how recovery and death rates evolved.

The project uses Python for data processing and visualization, along with Streamlit to create an interactive dashboard for users.

---

## 🎯 Objectives
- Analyze the growth of COVID-19 cases over time  
- Identify the most affected countries  
- Compare death and recovery trends  
- Study daily case fluctuations to identify waves  
- Provide an interactive platform for users to explore data  

---

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **Pandas** – Data cleaning and manipulation  
- **Matplotlib** – Data visualization  
- **Streamlit** – Interactive web dashboard  

---

## 📊 Features

### 🔹 Data Analysis
- Processes real-world COVID-19 dataset  
- Groups and analyzes data based on time  

### 🔹 Visualizations
- 📈 Total cases over time  
- 🌍 Top 10 affected countries  
- ⚰️ Death vs Recovery comparison  
- 📉 Daily new cases trend  

### 🔹 Interactive Dashboard
- Upload your own CSV dataset  
- Enter dataset URL  
- Dynamic graph updates  
- Dynamic descriptions and insights  

### 🔹 User-Friendly Design
- Simple explanations for each graph  
- Key statistics displayed  
- Insights for better understanding  

---

## 📁 Project Structure
COVID-Analysis/
│
├── analysis.py # Generates graphs using matplotlib
├── app.py # Streamlit interactive dashboard
├── covid.csv # Dataset file
└── README.md

---

## ▶️ How to Run the Project

### Step 1: Install Required Libraries
pip install pandas matplotlib streamlit

### Step 2: Run Data Analysis Script
python analysis.py

### Step 3: Launch Dashboard
streamlit run app.py

---

## 📌 Dataset Information
The dataset includes the following columns:
- Date  
- Country  
- Confirmed Cases  
- Deaths  
- Recovered Cases 

---

## 🚀 Conclusion
This project demonstrates how data visualization can help in understanding complex real-world problems like the COVID-19 pandemic. The interactive dashboard makes it easier for users to explore trends and gain meaningful insights.

---

## 👨‍💻 Author
Arun Maity
