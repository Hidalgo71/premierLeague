import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# NOTES
# Hue is a plot list name

eplData = pd.read_csv("E:\PycharmProjects\premierLeague\premier-league\stats.csv")
# print(eplData.head(10))
sb.countplot('wins', data=eplData)
# plt.show()

# print(eplData.groupby(['team', 'total_red_card'])['total_red_card'].count())

# eplData[['team', 'own_goals']].groupby(['team']).mean().plot.bar()
sb.countplot('team', hue='own_goals', data=eplData, )
# plt.show()

# sb.countplot('clean_sheet', hue='team', data=eplData)
plt.title('Clean Sheet teams')
plt.show()

print('Most Goal: ', eplData['goals'].max())
print('Least Goal: ', eplData['goals'].min())
print('Average Goal: ', eplData['goals'].mean())

# sb.violinplot("total_yel_card", "total_red_card", hue="team", data=eplData, split=True)
plt.show()