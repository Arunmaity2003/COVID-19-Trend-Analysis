import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Styling
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (10, 5)

# Load dataset
df = pd.read_csv("covid.csv")

print("First 5 rows:")
print(df.head())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by date (global data)
global_data = df.groupby('Date').sum(numeric_only=True)

# ------------------ GRAPH 1 ------------------
plt.figure()
plt.plot(global_data.index, global_data['Confirmed'], color='blue')

plt.title("Total COVID-19 Cases Over Time", fontsize=14, fontweight='bold')
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("cases_over_time.png")

print("Graph saved as cases_over_time.png")


# ------------------ GRAPH 2 ------------------
latest_data = df[df['Date'] == df['Date'].max()]
top_countries = latest_data.sort_values(by='Confirmed', ascending=False).head(10)

plt.figure()
plt.bar(top_countries['Country'], top_countries['Confirmed'], color='orange')

plt.title("Top 10 Most Affected Countries", fontsize=14, fontweight='bold')
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_countries.png")

print("Top 10 countries graph saved as top_10_countries.png")


# ------------------ GRAPH 3 ------------------
plt.figure()
plt.plot(global_data.index, global_data['Deaths'], label='Deaths', color='red')
plt.plot(global_data.index, global_data['Recovered'], label='Recovered', color='green')

plt.title("Deaths vs Recovered Over Time", fontsize=14, fontweight='bold')
plt.xlabel("Date")
plt.ylabel("Count")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("deaths_vs_recovered.png")

print("Deaths vs Recovered graph saved as deaths_vs_recovered.png")


# ------------------ GRAPH 4 ------------------
global_data['Daily New Cases'] = global_data['Confirmed'].diff()

plt.figure()
plt.plot(global_data.index, global_data['Daily New Cases'], color='purple')

plt.title("Daily New COVID-19 Cases", fontsize=14, fontweight='bold')
plt.xlabel("Date")
plt.ylabel("Daily Cases")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_new_cases.png")

print("Daily new cases graph saved as daily_new_cases.png")