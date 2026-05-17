import pandas as pd
import matplotlib.pyplot as plt

#Load Dataset
batters = pd.read_csv("IPL2025Batters.csv")
bowlers = pd.read_csv("IPL2025Bowlers.csv")

#View Dataset
# print(batters.info())
# print(batters.describe())
# print(batters.head())
# print(batters.isnull().sum())

# print(bowlers.info())
# print(bowlers.describe())
# print(bowlers.head())
# print(bowlers.isnull().sum())

#Convert column names into more readable
batters.columns = ["Player","Team","Runs","Matches","Innings","NotOuts",
    "HighestScore","Average","BallsFaced","StrikeRate","Hundreds",
    "Fifties","Fours","Sixes"]

bowlers.columns = ["Player","Team","Wickets","Matches",
    "Innings","Overs","RunsConceded","BestBowling",
    "Average","Economy","StrikeRate","FourWickets","FiveWickets"
    ]
# print(batters.dtypes)
# print(bowlers.dtypes)

#Convert Batting Average into float for future analysis
batters["Average"] = pd.to_numeric(batters["Average"],errors="coerce")

#Top Run Scorers
top_run = batters.sort_values(by="Runs",ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.bar(top_run["Player"],top_run["Runs"],color="skyblue")
plt.title("Top 10 Run Scorers in IPL 2025")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.grid(axis="y",linestyle="--",alpha=0.5)
for i, v in enumerate(top_run["Runs"]):
    plt.text(i, v + 5, str(v), ha='center')
plt.tight_layout()
# plt.show()
plt.close()

#Top Six Hitters
plt.figure(figsize=(12,6))
top_sixes = batters.sort_values(by="Sixes",ascending=False).head(10)
plt.bar(top_sixes["Player"],top_sixes["Sixes"],color="crimson")
plt.title("Top 10 players with Most 6's in IPL 2025")
plt.xlabel("Players")
plt.ylabel("Sixes")
plt.xticks(rotation=45)
plt.grid(axis="y",linestyle = "--",alpha=0.5)
for i,v in enumerate(top_sixes["Sixes"]):
    plt.text(i,v+4,str(v),ha="center")
plt.tight_layout()
# plt.show()
plt.close()

#Highest Strike Rate Players
qualified = batters[batters["BallsFaced"] > 100]
top_sr = qualified.sort_values(by="StrikeRate",ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.barh(top_sr["Player"],top_sr["StrikeRate"],color="pink")
plt.title("Top 10 players with highest Strike Rate in IPL 2025")
plt.xlabel("Strike Rate")
plt.ylabel("Players")
plt.grid(axis="x",linestyle="--",alpha=0.5)
for i,v in enumerate(top_sr["StrikeRate"]):
    plt.text(v+1,i,str(round(v,1)))
# plt.show()
plt.close()

#Team wise Total Runs
team = batters.groupby("Team")["Runs"].sum().sort_values(ascending=False)
plt.figure(figsize=(12,6))
plt.bar(team.index,team.values,color="skyblue")
plt.title("Team wise score in IPL2025")
plt.xlabel("Team")
plt.ylabel("Total Runs")
plt.grid(axis="y",linestyle="--",alpha=0.5)
for i,v in enumerate(team.values):
    plt.text(i,v+5,str(v),ha="center")
# plt.show()
plt.close()

#Top Wicket Takers in IPL 2025
highest_wicket = bowlers.sort_values(by="Wickets",ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.bar(highest_wicket["Player"],highest_wicket["Wickets"],color="skyblue")
plt.title("Highest Wicket takers of IPL2025")
plt.xlabel("Players")
plt.ylabel("Wickets")
plt.xticks(rotation=45)
plt.grid(axis="y",linestyle="--",alpha=0.5)
for i,v in enumerate(highest_wicket["Wickets"]):
    plt.text(i,v+1,str(v),ha="center")
# plt.show()
plt.close()

# Best Economy in IPL2025
qualified_bowlers = bowlers[bowlers["Overs"]>10]
best_eco = qualified_bowlers.sort_values(by="Economy",ascending=True).head(10).reset_index()
plt.barh(best_eco["Player"],best_eco["Economy"],color="violet")
plt.title("Best Economy Bowlers of IPL2025")
plt.xlabel("Economy")
plt.ylabel("Player")
plt.grid(axis="x",linestyle="--",alpha=0.5)
for i,v in enumerate(best_eco["Economy"]):
    plt.text(v+0.1,i,str(round(v,2)))
# plt.show()
plt.close()

# Runs vs Strike Rate
qualified = batters[batters["Runs"]>100].head(10)
plt.scatter(qualified["Runs"],qualified["StrikeRate"])
plt.title("Runs vs Strike Rate")
plt.xlabel("Runs")
plt.ylabel("Strike Rate")
plt.grid(linestyle="--",alpha=0.5)
for i in range(10):
    plt.text(qualified["Runs"].iloc[i],qualified["StrikeRate"].iloc[i],qualified["Player"].iloc[i],fontsize=7)
plt.tight_layout()
# plt.show()
plt.close()

# Groups of Runs Scored(in ranges)
plt.figure(figsize=(10,6))
counts,bins,patches = plt.hist(batters["Runs"],bins=10,color="green",edgecolor="black")
plt.title("Distribution of Runs - IPL 2025")
plt.xlabel("Runs")
plt.ylabel("Number of Players")
plt.grid(axis="y",linestyle="--",alpha=0.5)
for count, patch in zip(counts, patches):  
    plt.text(patch.get_x() + patch.get_width()/2,count,int(count),ha='center',va='bottom')
# plt.show()
plt.close()

#Subplots of most runs and wickets

#1st graph
fig,ax = plt.subplots(1,2,figsize=(15,6))
ax[0].bar(top_run["Player"],top_run["Runs"],color="blue")
ax[0].set_title("Top Run Scorers")
ax[0].set_xlabel("Player")
ax[0].set_ylabel("Runs")
ax[0].tick_params(axis="x",rotation=45)

#2nd graph
ax[1].bar(highest_wicket["Player"], highest_wicket["Wickets"],color="green")
ax[1].set_title("Top Wicket Takers")
ax[1].set_xlabel( "Players")
ax[1].set_ylabel("Wickets")
ax[1].tick_params( axis='x',rotation=45)
plt.tight_layout()
# plt.show()
plt.close()

#Correlation 
numeric_batter = batters.select_dtypes(include=["int64","float64"])
corr_matrix = numeric_batter.corr()
plt.figure(figsize=(10,8))
plt.imshow(corr_matrix)
plt.colorbar()
plt.xticks(range(len(corr_matrix)),corr_matrix.columns,rotation=45)
plt.yticks(range(len(corr_matrix.columns)),corr_matrix.columns)
plt.title("Correlation Matrix - IPL2025")
plt.tight_layout()
# plt.show()
plt.close()

#Box plot - Runs
plt.figure(figsize=(8,5))
plt.boxplot(batters["Runs"],patch_artist=True)
plt.title("Distribution of Runs - IPL 2025")
plt.ylabel("Runs")
# plt.show()
plt.close()

# Horizontal Box plots - Wickets
plt.figure(figsize=(8,5))
plt.boxplot(bowlers["Economy"],vert=False)
plt.title("Economy Distribution - IPL 2025")
plt.xlabel("Economy")
# plt.show()
plt.close()

# Multi box plot
plt.figure(figsize=(8,5))
plt.boxplot([batters["Runs"],batters["BallsFaced"],batters["StrikeRate"]])
plt.xticks( [1,2,3], ["Runs","Balls Faced","Strike Rate"])
plt.ylabel("Values")
plt.title("Comparison of Batting Metrics - IPL 2025")
# plt.show()
plt.close()

# Pie Chart of Runs by Team
plt.figure(figsize=(8,8))
plt.pie(team,labels=team.index,autopct="%1.1f%%")
plt.title("Runs Contribution by Teams - IPL 2025")
# plt.show()
plt.close()

#Pie Chart of 4's
top4s = batters.sort_values(by="Fours",ascending=False).head(10)
plt.figure(figsize=(8,8))
plt.pie(top4s["Fours"],labels=top4s["Player"],autopct="%1.1f%%")
plt.title("4's contribution by Top 10 players - IPL 2025")
# plt.show()
plt.close()

#Line Plot of most runs
plt.figure(figsize=(10,5))
plt.plot(top_run["Player"],top_run["Runs"], marker="o")
plt.title("Top 10 Batters by Runs - IPL 2025")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.grid()
# plt.show()
plt.close()

# Line plot of most wickets
plt.figure(figsize=(10,5))
plt.plot(highest_wicket["Player"],highest_wicket["Wickets"],marker="o")
plt.title("Top 10 Players by Wickets - IPL 2025")
plt.xlabel("Players")
plt.ylabel("Wickets")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
# plt.show()
plt.close()

# Stacked Bar Charts

plt.figure(figsize=(10,5))
runs_from_4s = top_run["Fours"]*4
runs_from_6s = top_run["Sixes"]*6
plt.bar(top_run["Player"],runs_from_4s,label="Run from 4s")
plt.bar(top_run["Player"],runs_from_6s,bottom=runs_from_4s,label="Runs from 6s")
plt.title("Boundary Contribution of Top 10 Players - IPL 2025")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()
plt.close()

#Advanced scatter customizations - point = sixes , color = Average
plt.figure(figsize=(12,8))
scatter = plt.scatter(qualified["Runs"],qualified["StrikeRate"],
                      s=qualified["Sixes"]*2,c=qualified["Average"],alpha=0.5)
plt.colorbar(scatter)
plt.title("Runs Vs Strike Rate Advanced Scatter - point = sixes , color = Average")
plt.xlabel("Runs")
plt.ylabel("Strike Rate")
for i,player in enumerate(qualified["Player"]):
    plt.text(qualified["Runs"].iloc[i],qualified["StrikeRate"].iloc[i]+1,player,ha="center",fontsize=8)
plt.grid()
# plt.show()
plt.close()

# Legend 
plt.figure(figsize=(10,6))
plt.plot(top_run["Player"],top_run["Runs"],label="Runs",marker="o")
plt.plot(top_run["Player"],top_run["StrikeRate"],label="Strike Rate",marker="o")
plt.xticks(rotation=45)
plt.legend()
plt.show()
plt.close()

