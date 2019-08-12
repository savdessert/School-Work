
"""
Created on Wed Apr 24 08:27:32 2019
Using video game sales data, condition and create meaningful graphs of relevent fields to analyze trends in the data.
"""

import matplotlib.pyplot as plt
import pandas as pd

gamedata = pd.read_csv("./.spyder-py3/Video_Games_Sales.csv")
region = gamedata.loc[:,"NA_Sales":"Other_Sales"]
Region_Counts= region.sum()
labels = Region_Counts.index.tolist()

plt.barh(labels, Region_Counts)
plt.tight_layout()
plt.xlabel("Sales in millions")
plt.title("Game Sales by Region")
plt.gca().invert_yaxis()
plt.show()

Genre_Counts = gamedata["Genre"].value_counts()
labels = Genre_Counts.index.tolist()

plt.barh(labels, Genre_Counts)
plt.tight_layout()
plt.xlabel("Sales in millions")
plt.title("Game Sales by Genre")
plt.gca().invert_yaxis()
plt.show()

#Pie Charts for each genre showing regional sales
gamedata.set_index("Genre", inplace = True)

Action = gamedata.loc["Action", "NA_Sales":"Other_Sales"]
Sales = Action.sum()
Regions = Action.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Action Sales by Region")
plt.show()

Sports = gamedata.loc["Sports", "NA_Sales":"Other_Sales"]
Sales = Sports.sum()
Regions = Sports.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Sports Sales by Region")
plt.show()

Misc = gamedata.loc["Misc", "NA_Sales":"Other_Sales"]
Sales = Misc.sum()
Regions = Misc.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Misc Sales by Region")
plt.show()

RPG = gamedata.loc["Role-Playing", "NA_Sales":"Other_Sales"]
Sales = RPG.sum()
Regions = RPG.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("RPG Sales by Region")
plt.show()

Shooter = gamedata.loc["Shooter", "NA_Sales":"Other_Sales"]
Sales = Shooter.sum()
Regions = Shooter.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Shooter Game Sales by Region")
plt.show()

Adventure = gamedata.loc["Adventure", "NA_Sales":"Other_Sales"]
Sales = Adventure.sum()
Regions = Adventure.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Adventure Game Sales by Region")
plt.show()

Racing = gamedata.loc["Racing", "NA_Sales":"Other_Sales"]
Sales = Racing.sum()
Regions = Racing.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Racing Game Sales by Region")
plt.show()

Platform = gamedata.loc["Platform", "NA_Sales":"Other_Sales"]
Sales = Platform.sum()
Regions = Platform.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Platform Game Sales by Region")
plt.show()

Simulation = gamedata.loc["Simulation", "NA_Sales":"Other_Sales"]
Sales = Simulation.sum()
Regions = Simulation.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Simulation Game Sales by Region")
plt.show()

Fighting = gamedata.loc["Fighting", "NA_Sales":"Other_Sales"]
Sales = Fighting.sum()
Regions = Fighting.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Fighting Game Sales by Region")
plt.show()

Strategy = gamedata.loc["Strategy", "NA_Sales":"Other_Sales"]
Sales = Strategy.sum()
Regions = Strategy.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Strategy Game Sales by Region")
plt.show()

Puzzle = gamedata.loc["Puzzle", "NA_Sales":"Other_Sales"]
Sales = Puzzle.sum()
Regions = Puzzle.sum().index.tolist()
patches, texts, autotexts = plt.pie(Sales, shadow=True, autopct='%.1f%%', pctdistance=.8, textprops={'color':"w"})
plt.legend(patches, Regions, title="Regions",loc="center left",bbox_to_anchor=(1, 0, 0.5, 1))
plt.title("Puzzle Game Sales by Region")
plt.show()





