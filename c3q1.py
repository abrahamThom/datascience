import matplotlib.pyplot as plt

years= [2001,2002,2003,2004,2005,2006,2007]
car_values = [24000,22500,19700,17500,14500,10000,5800]

plt.figure(figsize=(10, 6))

plt.subplot(111)
plt.plot(years, car_values, linestyle='-.', color='red', marker='*',markersize=20,markerfacecolor='green')
plt.title("Value Depreciation", loc="left")
plt.xlabel("Year")
plt.ylabel("Car Value")

plt.savefig('fig.png')
