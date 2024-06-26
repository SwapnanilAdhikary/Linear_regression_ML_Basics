# -*- coding: utf-8 -*-
"""Linear_Regression

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ywpXR8ePfK6q8-_RWc3QxbGdZareoJ3p
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("homeprices.csv")

df

plt.xlabel('Area(sqr ft)')
plt.ylabel('Price(US$)')
plt.scatter(df.Area,df.Price,color="red",marker='+')

reg = LinearRegression()
reg.fit(df[['Area']],df.Price)

reg.predict([[3300]])



