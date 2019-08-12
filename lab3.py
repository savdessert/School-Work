"""
Savannah Dessert, cssc0696
https://www.kaggle.com/zynicide/wine-reviews/version/4
This dataset contains information from 150k 4-5 star rated wines including where the wine was produced.
I want to use the "country" and "province" headers to plot the amount of different wines by region in France with a pie chart.
"""
import matplotlib.pyplot as plt
import pandas as pd

winedata = pd.read_csv("./.spyder-py3/winemag-data_first150k.csv")

winedata.set_index("country", inplace=True)
regions = winedata.loc["France", "province"]

counts = regions.value_counts()
labels = regions.value_counts().index.tolist()

patches, texts, autotexts = plt.pie(counts, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, labels, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("French Wine Production by Region")
plt.show()
