import seaborn as sns
import matplotlib.pyplot as plt
import os

colours = ["#E63946", "#1D3557", "#457B9D", "#A8DADC"]

# general information
export_folder = "taipei"
file_name = "electricity"

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
# autopct: for adding percentages in the figure, ".1f" means one digit
# textprops: adding labels to the parts
plot = plt.pie(data, labels=keys, autopct='%.1f%%', textprops={'fontsize': 14, 'color': "#F1FAEE"})

# export
path = f"./export/{export_folder}"

if not os.path.exists(path):
    os.makedirs(path)

plt.savefig(f"{path}/{file_name}.png", transparent=True, dpi=300,)

# show figure
plt.show()