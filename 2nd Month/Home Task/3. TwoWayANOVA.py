import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 1. Teaching Method x Gender (Education)
method = ["Lecture"]*6 + ["Online"]*6 + ["Blended"]*6
gender = ["Male"]*3 + ["Female"]*3
gender = gender * 3
score = [60,62,65, 58, 59, 61, 70,72,74, 68, 69, 71, 80, 82, 85, 78,79,81]
df = pd.DataFrame({"method": method, "gender": gender, "score": score})
model = ols('score ~ C(method) * C(gender)', data=df).fit()
print(sm.stats.anova_lm(model))


# 2. Machine Type x Shift (Manufacturing)
machine = ["A"]*6 + ["B"]*6 + ["C"]*6
shift = ["Day"]*3 + ["Night"]*3
shift = shift * 3
output = [20, 22, 21, 18, 19, 20, 25,27,26, 23, 24, 25, 30,32,31, 28,29,30]
df = pd.DataFrame({"machine": machine, "shift": shift, "output": output})
model = ols('output ~ machine * shift', data=df).fit()
print(sm.stats.anova_lm(model))



# 3. Campaign x Region (Marketing)
campaign = ["Social"]*6 + ["TV"]*6 + ["Email"]*6
region = ["Urban"]*3 + ["Rural"]*3
region = region * 3
sales = [200, 210, 205, 180, 190,185, 250,260,255, 230,240,235, 170, 175, 180, 160,165,170]
df = pd.DataFrame({"campaign": campaign, "region": region, "sales": sales})
model = ols('sales ~ campaign * region', data=df).fit()
print(sm.stats.anova_lm(model))



# 4. Drug x Dosage (Healthcare)
drug = ["D1"]*6 + ["D2"]*6 + ["D3"]*6
dose = ["Low"]*3 + ["High"]*3
dose = dose * 3
recovery = [5,6,7, 8,9,10, 6,7,8, 9,10,11, 4,5,6, 7,8,9]
df = pd.DataFrame({"drug": drug, "dose": dose, "recovery": recovery})
model = ols('recovery ~ drug * dose', data=df).fit()
print(sm.stats.anova_lm(model))



# 5. Store Type x Location (Retail)
store = ["Supermarket"]*6 + ["Mall"]*6 + ["Online"]*6
location = ["City"]*3 + ["Town"]*3
location = location * 3
revenue = [500,520,510, 480,490,495, 600, 620, 610, 580,590,600, 550,560,570, 530,540,545]
df = pd.DataFrame({"store": store, "location": location, "revenue": revenue})
model = ols('revenue ~ store * location', data=df).fit()
print(sm.stats.anova_lm(model))



# 6. Study Hours x Teaching Style
hours = ["Low"]*6 + ["Medium"]*6 + ["High"]*6
style = ["Traditional"]*3 + ["Modern"]*3
style = style * 3
marks = [50,52,55, 48, 49, 51, 65, 67, 66, 63, 64, 65, 80, 82, 81, 78, 79, 80]
df = pd.DataFrame({"hours": hours, "style": style, "marks": marks})
model = ols('marks ~ hours * style', data=df).fit()
print(sm.stats.anova_lm(model))



# 7. Fuel Type x Engine Size
fuel = ["Petrol"]*6 + ["Diesel"]*6 + ["Hybrid"]*6
engine = ["Small"]*3 + ["Large"]*3
engine = engine * 3
efficiency = [12,13,11, 10, 11, 12, 15,16,14, 13,14,15, 20, 22, 21, 18, 19, 20]
df = pd.DataFrame({"fuel": fuel, "engine": engine, "efficiency": efficiency})
model = ols('efficiency ~ fuel * engine', data=df).fit()
print(sm.stats.anova_lm(model))




# 8. Fertilizer x Soil Type (Agriculture)
fertilizer = ["F1"]*6 + ["F2"]*6 + ["F3"]*6
soil = ["Clay"]*3 + ["Sandy"]*3
soil = soil * 3
yield_ = [30,32,31, 28, 29, 30, 35,37,36, 33, 34, 35, 25,27,26, 23,24,25]
df = pd.DataFrame({"fertilizer": fertilizer, "soil": soil, "yield": yield_})
model = ols('yield ~ fertilizer * soil', data=df).fit()
print(sm.stats.anova_lm(model))



# 9. Department x Experience Level (HR)
dept = ["HR"]*6 + ["IT"]*6 + ["Finance"]*6
experience = ["Junior"]*3 + ["Senior"]*3
experience = experience * 3
performance = [60, 62, 61, 65, 66, 67, 75,78,77, 80, 82, 81, 70, 72, 71, 74,75,76]
df = pd.DataFrame({"dept": dept, "experience": experience, "performance": performance})
model = ols('performance ~ dept * experience', data=df).fit()
print(sm.stats.anova_lm(model))



# 10. Process x Temperature (Engineering)
process = ["P1"]*6 + ["P2"]*6 + ["P3"]*6
temp = ["Low"]*3 + ["High"]*3
temp = temp * 3
strength = [100,102,101, 95, 96, 97, 110, 112, 111, 105, 106, 107, 90, 92, 91, 85, 86, 87]
df = pd.DataFrame({"process": process, "temp": temp, "strength": strength})
model = ols('strength ~ process * temp', data=df).fit()
print(sm.stats.anova_lm(model))
