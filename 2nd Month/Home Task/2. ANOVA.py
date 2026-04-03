import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 1. Teaching Methods (Education)

method = ["Lecture"]*5 + ["Online"]*5 + ["Blended"]*5
scores = [60,65,70,62,68, 72,75,78,74,77, 80,82,85,83,88]

df_blue = pd.DataFrame({"method": method, "scores": scores})

sns.boxplot(x="method", y="scores", data=df_blue, color="skyblue")
plt.show()

anova_model = ols('scores ~ method', data=df_blue).fit()
print(anova_model.summary())

# 2. Machine Types Manufacturing

machine = ["A"]*6 + ["B"]*6 + ["C"]*6
output = [20,77,19,23,21,20, 25,22,26,28,29,30, 18,17,19,16,20,18]

df_orange = pd.DataFrame({"machine": machine, "output": output})

sns.boxplot(x="machine", y="output", data=df_orange, color="orange")
plt.show()

anova_model = ols('output ~ machine', data=df_orange).fit()
print(anova_model.summary())

# 3. Marketing Campaigns

campaign = ["Social"]*5 + ["TV"]*5 + ["Email"]*5
sales = [200,210,190,205,198, 250,260,255,270,265, 180, 175, 190,185,178]

df_green = pd.DataFrame({"campaign": campaign, "sales": sales})

sns.boxplot(x="campaign", y="sales", data=df_green, color="green")
plt.show()

anova_model = ols('sales ~ campaign', data=df_green).fit()
print(anova_model.summary())

# 4. Student Groups

group = ["A"]*4 + ["B"]*4 + ["C"]*4
marks = [55,60,58,62, 65,68,70,66, 75,78,80,77]

df_purple = pd.DataFrame({"group": group, "marks": marks})

sns.boxplot(x="group", y="marks", data=df_purple, color="purple")
plt.show()

anova_model = ols('marks ~ group', data=df_purple).fit()
print(anova_model.summary())

# 5. Drug Effectiveness

drug = ["Drug1"]*5 + ["Drug2"]*5 + ["Drug3"]*5
recovery = [5,6,7,5,6,8,9,7,8,9,6,7,6,7,8]

df_red = pd.DataFrame({"drug": drug, "recovery": recovery})

sns.boxplot(x="drug", y="recovery", data=df_red, color="red")
plt.show()

anova_model = ols('recovery ~ drug', data=df_red).fit()
print(anova_model.summary())

# 6. Store Location

location = ["Urban"]*5 + ["Suburban"]*5 + ["Rural"]*5
revenue = [500,520,510,530,515, 450,460,470,455,465, 400, 420, 410,405,415]

df_cyan = pd.DataFrame({"location": location, "revenue": revenue})

sns.boxplot(x="location", y="revenue", data=df_cyan, color="cyan")
plt.show()

anova_model = ols('revenue ~ location', data=df_cyan).fit()
print(anova_model.summary())
