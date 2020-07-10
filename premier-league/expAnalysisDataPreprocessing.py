import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

eplData = pd.read_csv("E:\PycharmProjects\premierLeague\premier-league\stats.csv")

print(eplData.shape)
print(eplData.describe())
print(eplData.info())

# Any columns with missing value
nullColm = eplData.columns[eplData.isnull().any()]
print(eplData.isnull().sum())

plt.scatter(eplData.big_chance_missed, eplData.goals, alpha=0.1)
plt.title("Big misssed goals")
# plt.show()

# Histogram graph probability distribution for features
eplData.hist(bins=10, figsize=(9, 7), grid=False)

# See x rate

# g = sns.FacetGrid(eplData, col="team", row="losses", margin_titles=True)
# g.map(plt.hist, "team", color="cyan")

print("===================================")

# g = sns.FacetGrid(eplData, hue="team", col="clean_sheet", margin_titles=True,
#                  palette={1: "seagreen", 0: "gray"})
# g = g.map(plt.scatter, "wins", "loses", edgecolor="w").add_legend()

ax = sns.boxplot(x="team", y="total_pass", data=eplData)
ax = sns.stripplot(x="team", y="total_pass", data=eplData,
                   jitter=True, edgecolor="gray")

g = sns.FacetGrid(eplData, hue="team", col="goals", margin_titles=True,
                  palette="Set1", hue_kws=dict(marker=["^", "v"]))
g.map(plt.scatter, "own_goals", "goals_conceded", edcolor="w").add_legend()
plt.subplots_adjust(top=0.8)
g.fig.suptitle('Team by goals, Own and goals conceded')