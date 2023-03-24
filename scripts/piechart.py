import seaborn as sns
import matplotlib.pyplot as plt
import os

colours = ["#E63946", "#1D3557", "#457B9D", "#A8DADC"]

# general information
city = "taipei"
topic = "electricity"
#title = "Exports of Taiwan"

# declaring data \n
data = [44.9, 36.4, 9.6]
keys = ['Coal', 'Gas', 'Nuclear']

data_sum = sum(data)
data.append(100 - data_sum)
keys.append("Renewables")


# formats
plt.style.use("dark_background")
sns.set(style="darkgrid", context="talk", font="Roboto", palette=colours, rc={'axes.facecolor': 'black', 'figure.facecolor': 'black'})
#sns.set_palette(sns.color_palette(colours))
#plt.title(f"{title}", y=1.05, fontsize=20, color="#F1FAEE")

# plotting data on chart
plot = plt.pie(data, labels=keys, autopct='%.0f%%', textprops={'fontsize': 14, 'color': "#F1FAEE"})

#plot.set(xlabel=None)
#plot.set(ylabel=None)
#sns.despine(left=True)

path = f"./export/{city}"

if not os.path.exists(path):
    os.makedirs(path)

plt.savefig(f"{path}/{topic}.png", transparent=True, dpi=300,)

# show
plt.show()