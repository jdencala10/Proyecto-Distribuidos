import requests
import matplotlib.pyplot as plt
import numpy as np


tiemposSinCache = []
tiemposConCache = []
for x in range(10):
	response = requests.get('http://18.191.229.197/')
	tiemposSinCache.append(response.elapsed.total_seconds())
for y in  range(10):
	response2=requests.get('http://18.191.229.197/1')
	tiemposConCache.append(response2.elapsed.total_seconds())
print(tiemposSinCache)
print("-"*20)
print(tiemposConCache)

plt.figure()
plt.boxplot(np.array(tiemposSinCache), 0, '')
plt.show()
