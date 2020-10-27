import pandas as pd
# import matplotlib.pyplot as plt

# # Make the graphs a bit prettier, and bigger
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (15, 5) 

df = pd.read_csv("C:\\Users\\arerlend\\Downloads\\COVID-19_Case_Surveillance_Public_Use_Data.csv", nrows=10)

print(df)