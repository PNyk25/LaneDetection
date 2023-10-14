import matplotlib.pyplot as plt 
import pandas as pd 
data = pd.read_csv('co2_emission.csv') 
subset_data = data.head(10) 
values = subset_data.iloc[:, 1] 
plt.hist(values, bins=5, color='m') 
plt.title("CO2 Emission by Vehicle Type") 
plt.xlabel("Vehicle Type") 
plt.ylabel("Count") 
plt.show()