import pandas as pd
from weatherClass import weather as w
model = w()
df= pd.read_csv("weather.csv")
print(df)
