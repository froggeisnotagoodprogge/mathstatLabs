import numpy
from scipy.stats import norm
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as statsm

data = pandas.read_csv("/Users/frogge/proggs/mathstatLabs/lab-1/mobile_phones.csv")
# how many models are available to install 2 sim cards
print(data['dual_sim'].sum())

# how many models support 3-G
print(data['three_g'].sum())

# maximum number of cores
print(data['n_cores'].max())

new_data = data['battery_power']
#new_data = data[data['wifi'] == 1]['battery_power']
#new_data = data[data['wifi'] == 0]['battery_power']

# selective mean
print(round(new_data.mean(), 4))

# dispersion
print(round(new_data.var(), 4))

# median
print(round(new_data.median(), 4))

# quantile 2/5
print(round(new_data.quantile(q = 0.4), 4))

x = numpy.linspace(min(new_data), max(new_data))
y = statsm.distributions.ECDF(new_data)(x)
plt.step(x, y)
plt.title("Graph of ecdf")
plt.show()
#plt.hist(new_data, histtype='step', cumulative=True, bins=len(sample))     -     another way to plot a graph

plt.hist(new_data)
plt.title("Histogram")
plt.show()

plt.boxplot(new_data)
plt.title("Box-plot")
plt.show()