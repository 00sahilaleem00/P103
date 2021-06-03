import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
fig = px.scatter(df, x="date", y="cases", colour="country",
                 size="country", size_max=20)
fig.show()
