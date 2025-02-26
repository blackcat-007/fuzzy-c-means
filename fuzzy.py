import pandas as pd  
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sb
filename='housing.csv'
data=pd.read_csv(filename)
print(data.head(5))

data=data.loc[:,['latitude','longitude']]
plt.scatter(data.latitude,data.longitude)