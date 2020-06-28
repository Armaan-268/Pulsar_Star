import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Plot_1
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,0].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()

# Plot_2
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,1].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()

# Plot_3
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,2].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()

# Plot_4
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,3].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()

# Plot_5
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,4].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()

# Plot_6
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,5].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()

# Plot_7
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,6].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()

# Plot_8
x = pd.read_csv('pulsar_stars.csv')
x = x.iloc[:,7].values
y = pd.read_csv('pulsar_stars.csv')
y = y.iloc[:,-1].values
plt.scatter(x,y)
plt.xlabel('Data Values')
plt.ylabel('Target Class')
plt.show()