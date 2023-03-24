import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

# datasource: https://worldpopulationreview.com/world-cities/
colours = ["#E63946", "#1D3557", "#457B9D", "#A8DADC"]

city = "taipei"
topic = "population"

# import data
data = pd.read_csv(f'data/{city}.csv')

# format
#sns.set(rc={'figure.figsize':(8, 6)})
sns.set(style="darkgrid", context="talk", font="Roboto", palette=colours, rc={'axes.facecolor': 'black', 'figure.facecolor': 'black', 'figure.figsize': (10, 6)})
#sns.set_palette("pastel")
#plt.style.use("dark_background")
#plt.title("Population in Taipei", y=1.05, fontsize=20, color="#F1FAEE")

# plot
plot = sns.lineplot(data=data, x="year", y="population", lw=4)
#textprops={'fontsize': 14, 'color': "#F1FAEE"}

plot.set(xlabel=None)
plot.set(ylabel=None)
sns.despine(left=True, bottom=True)

plot.tick_params(axis='both', labelsize=14, colors='#F1FAEE')
plot.grid(color='#F1FAEE')

# 1000 separator
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

path = f"./export/{city}"

if not os.path.exists(path):
    os.makedirs(path)


# save
plt.savefig(f"{path}/{topic}.png", transparent=True, dpi=300)
#plt.savefig("plot.svg", transparent=False)

# show
plt.show()

print('Done.')