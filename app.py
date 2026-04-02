# https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("COVID-19 Data Analysis Dashboard")

# ------------------ DATA INPUT ------------------
st.sidebar.header("Upload or Enter Dataset")

uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])
file_url = st.sidebar.text_input("OR Enter CSV File URL")

# Load dataset
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

elif file_url != "":
    try:
        df = pd.read_csv(file_url)
    except:
        st.error("Invalid URL or file not accessible")
        st.stop()

else:
    st.warning("Please upload a CSV file or enter a dataset URL")
    st.stop()

# ------------------ PREPROCESS ------------------
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
else:
    st.error("Dataset must contain a 'Date' column")
    st.stop()

global_data = df.groupby('Date').sum(numeric_only=True)

# ------------------ DATA PREVIEW ------------------
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ------------------ KEY METRICS ------------------
st.subheader("Key Statistics")

total_cases = int(df['Confirmed'].max())
total_deaths = int(df['Deaths'].max())
total_recovered = int(df['Recovered'].max())

col1, col2, col3 = st.columns(3)

col1.metric("Total Cases", total_cases)
col2.metric("Total Deaths", total_deaths)
col3.metric("Total Recovered", total_recovered)

# ------------------ SIDEBAR OPTIONS ------------------
option = st.sidebar.selectbox(
    "Choose Analysis",
    ["Cases Over Time", "Top Countries", "Deaths vs Recovered", "Daily Cases"]
)

# ------------------ VISUALIZATIONS ------------------

# Graph 1
if option == "Cases Over Time":
    st.subheader("Total Cases Over Time")
    st.write("This graph shows how COVID-19 cases increased over time globally.")

    fig, ax = plt.subplots()
    ax.plot(global_data.index, global_data['Confirmed'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Cases")

    st.pyplot(fig)

# Graph 2
elif option == "Top Countries":
    st.subheader("Top 10 Countries")
    st.write("This chart shows the countries most affected by COVID-19.")

    latest = df[df['Date'] == df['Date'].max()]
    top = latest.sort_values(by='Confirmed', ascending=False).head(10)

    fig, ax = plt.subplots()
    ax.bar(top['Country'], top['Confirmed'])
    plt.xticks(rotation=45)

    st.pyplot(fig)

# Graph 3
elif option == "Deaths vs Recovered":
    st.subheader("Deaths vs Recovered")
    st.write("This graph compares deaths and recoveries over time.")

    fig, ax = plt.subplots()
    ax.plot(global_data.index, global_data['Deaths'], label='Deaths')
    ax.plot(global_data.index, global_data['Recovered'], label='Recovered')
    ax.legend()

    st.pyplot(fig)

# Graph 4
elif option == "Daily Cases":
    st.subheader("Daily New Cases")
    st.write("This graph shows daily new cases and highlights peaks (waves).")

    global_data['Daily'] = global_data['Confirmed'].diff()

    fig, ax = plt.subplots()
    ax.plot(global_data.index, global_data['Daily'])

    st.pyplot(fig)

# ------------------ INSIGHTS ------------------
st.subheader("Key Insights")

if option == "Cases Over Time":
    st.write("""
    - COVID-19 cases show a continuous upward trend.
    - The growth was rapid during peak pandemic periods.
    - Indicates exponential spread in early stages.
    """)

elif option == "Top Countries":
    st.write("""
    - A small number of countries contributed to most cases.
    - Highly populated countries show higher impact.
    - Indicates uneven global distribution of COVID-19.
    """)

elif option == "Deaths vs Recovered":
    st.write("""
    - Recovery cases increased faster than deaths over time.
    - Shows improvement in healthcare and treatment.
    - Death rate stabilized after initial surge.
    """)

elif option == "Daily Cases":
    st.write("""
    - Multiple peaks indicate different COVID-19 waves.
    - Sudden spikes show outbreak periods.
    - Helps identify high-risk time periods.
    """)