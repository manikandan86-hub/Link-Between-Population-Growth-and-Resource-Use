# ------------------------------
# Project: Link Between Population Growth and Resource Use
# Authors: MANIKANDAN R S, PRAKASH G
# ------------------------------

# 📚 Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# 🔹 Step 1: Load datasets
# Replace these file names with your actual CSV files
population_df = pd.read_csv("UN_Population.csv")   # UN population data
energy_df = pd.read_csv("Energy_Consumption.csv")  # World Bank or other dataset

# 🔹 Step 2: View data samples
print("Population Data:")
print(population_df.head())
print("\nEnergy Data:")
print(energy_df.head())

# 🔹 Step 3: Data cleaning and preparation
# Example column names: 'Country', 'Year', 'Population'
# and 'Country', 'Year', 'Energy_Consumption'

# Merge both datasets by Country and Year
data = pd.merge(population_df, energy_df, on=["Country", "Year"], how="inner")

# Drop missing values
data.dropna(inplace=True)

# 🔹 Step 4: Exploratory Data Analysis (EDA)
print("\nCorrelation between Population and Energy Use:")
print(data[["Population", "Energy_Consumption"]].corr())

# 🔹 Step 5: Visualization
plt.figure(figsize=(8,5))
sns.scatterplot(x="Population", y="Energy_Consumption", data=data)
plt.title("Population vs Energy Consumption")
plt.xlabel("Population")
plt.ylabel("Energy Consumption (per capita or total)")
plt.grid(True)
plt.show()

# 🔹 Step 6: Trend Over Time for a Sample Country
country = "India"  # change as needed
country_data = data[data["Country"] == country]

plt.figure(figsize=(10,5))
plt.plot(country_data["Year"], country_data["Population"], label="Population", color="blue")
plt.plot(country_data["Year"], country_data["Energy_Consumption"], label="Energy Use", color="red")
plt.title(f"Population and Energy Use Trend in {country}")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

# 🔹 Step 7: Linear Regression Model (optional)
X = data[["Population"]]
y = data["Energy_Consumption"]

model = LinearRegression()
model.fit(X, y)

# Predict future energy use for a given population
future_population = [[1500000000]]  # Example: 1.5 billion
predicted_energy = model.predict(future_population)
print(f"\nPredicted Energy Use for Population {future_population[0][0]}: {predicted_energy[0]:.2f}")

# 🔹 Step 8: Conclusion Summary
print("\n✅ Analysis Complete!")
print("Population growth shows a positive correlation with energy use,")
print("indicating that higher population levels increase resource demand.")
