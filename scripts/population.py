import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# datasource: https://worldpopulationreview.com/world-cities/

city = "taipei"

# import data
data = pd.read_csv(f'data/{city}.csv')

# format
#sns.set(rc={'figure.figsize':(8, 6)})
sns.set(style="darkgrid", context="talk", font="Roboto", rc={'figure.figsize': (10, 6)})
sns.set_palette("pastel")
plt.style.use("dark_background")
plt.title("Population in Taipei", y=1.05, fontsize=20)

# plot
plot = sns.lineplot(data=data, x="year", y="population", lw=4)

plot.set(xlabel=None)
plot.set(ylabel=None)
sns.despine(left=True)

# 1000 separator
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

# save
plt.savefig(f"./export/{city}.png", transparent=True, dpi=300)
#plt.savefig("plot.svg", transparent=False)

# show
plt.show()

print('Done.')