import matplotlib.pyplot as plt
import numpy as np

# Data
mode_transport = np.array(['Walking', 'Cycling', 'Car', 'Bus', 'Train'])
feq = np.array([29, 15, 35, 18, 3])


plt.bar(mode_transport, feq,width=0.1, color='green')

# Labels and Title
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Frequency of Different Modes of Transport')

# Save and show
plt.savefig('fig5.png')
plt.show()
