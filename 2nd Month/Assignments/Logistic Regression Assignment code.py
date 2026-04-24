# 2 **COMMON MASTER PIPELINE (Reusable for ALL cases)**
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Statsmodels (for inference like R glm)
import statsmodels.api as sm
# sklearn (for ML evaluation)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, roc_curve, roc_auc_score







# **1 Education: Study Hours vs Pass (FULL EXECUTION)**0


# Dataset
df = pd.DataFrame({
    "hours": [1,2,3,4,5,6,7,8,9,10],
    "pass": [0,0,0,1,0,1,1,1,1,1]
})


# Visualization (Logistic Curve)
plt.scatter(df ["hours"], df["pass"])
plt.plot(df["hours"], df["pred_prob"]) 
plt.title("Logistic Curve: Hours vs Pass") 
plt.xlabel("Hours")
plt.ylabel("Probability of Passing")
plt.show()





# STATISTICAL MODEL (GLM like R)


X = sm.add_constant(df["hours"])
y = df ["pass"]

model = sm.Logit(y, X).fit()
print (model.summary())

# Odds Ratio
odds_ratio= np.exp(model.params) 
print("\nodds Ratio:\n", odds_ratio)


# MACHINE LEARNING MODEL
#
clf = LogisticRegression()
clf.fit(df[["hours"]], y)


# Predictions 

df["pred_prob"] = clf.predict_proba(df[["hours"]]) [:,1]
df["pred_class"] = clf.predict(df [["hours"]])


# Evaluation

print("\nAccuracy:", accuracy_score (y, df["pred_class"]))
print("\nConfusion Matrix:\n", confusion_matrix(y, df ["pred_class"]))



# ROC Curve
fpr, tpr, _ = roc_curve (y, df["pred_prob"])
auc = roc_auc_score (y, df ["pred_prob"])



plt.plot(fpr, tpr)
plt.title(f" ROC Curve (AUC = {auc:.2f})")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()


# **APPLY SAME PIPELINE TO ALL DATASETS**



# **2 Attendance vs Pass**
df = pd.DataFrame({
  "attendance": [50,55,60,65,70,75,80,85,90,95],
  "pass": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["attendance"])
y = df["pass"]

model = sm.Logit(y, X).fit()
print(model.summary())

odds_ratio = np.exp(model.params)
print("\nOdds Ratio:\n", odds_ratio)

clf = LogisticRegression()
clf.fit(df[["attendance"]], y)

df["pred_prob"] = clf.predict_proba(df[["attendance"]])[:,1]
df["pred_class"] = clf.predict(df[["attendance"]])

plt.scatter(df["attendance"], y)
plt.plot(df["attendance"], df["pred_prob"])
plt.title("Attendance vs Pass")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()























# 3 Marketing Spend vs Purchase**
df = pd.DataFrame({
    "spend": [100,200,150,300,250,400,350,450,500,550],
    "purchase": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["spend"])
y = df["purchase"]

model = sm.Logit(y, X).fit()
print(model.summary())

odds_ratio = np.exp(model.params)
print("\nOdds Ratio:\n", odds_ratio)

clf = LogisticRegression()
clf.fit(df[["spend"]], y)

df["pred_prob"] = clf.predict_proba(df[["spend"]])[:,1]
df["pred_class"] = clf.predict(df[["spend"]])

plt.scatter(df["spend"], y)
plt.plot(df["spend"], df["pred_prob"])
plt.title("Spend vs Purchase")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()








#  4 Website Time vs Signup**
df = pd.DataFrame({
"time":[1,2,3,4,5,6,7,8,9,10],
"signup": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["time"])
y = df["signup"]

model = sm.Logit(y, X).fit()
print(model.summary())

odds_ratio = np.exp(model.params)
print("\nOdds Ratio:\n", odds_ratio)

clf = LogisticRegression()
clf.fit(df[["time"]], y)

df["pred_prob"] = clf.predict_proba(df[["time"]])[:,1]
df["pred_class"] = clf.predict(df[["time"]])

plt.scatter(df["time"], y)
plt.plot(df["time"], df["pred_prob"])
plt.title("Time vs Signup")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()



















# **5 Age vs Disease**
df = pd.DataFrame({
    "age": [20,25,30,35,40,45,50,55,60,65],
    "disease": [0,0,0,0,1,0,1,1,1,1]
})

X = sm.add_constant(df["age"])
y = df["disease"]

model = sm.Logit(y, X).fit()
print(model.summary())

odds_ratio = np.exp(model.params)
print("\nOdds Ratio:\n", odds_ratio)

clf = LogisticRegression()
clf.fit(df[["age"]], y)

df["pred_prob"] = clf.predict_proba(df[["age"]])[:,1]
df["pred_class"] = clf.predict(df[["age"]])

plt.scatter(df["age"], y)
plt.plot(df["age"], df["pred_prob"])
plt.title("Age vs Disease")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()















# **6  BMI vs Diabetes**


df = pd.DataFrame({
  "bmi": [18,20,22,24,26,28,30,32,34,36],
  "diabetes": [0,0,0,0,1,0,1,1,1,1]
})

X = sm.add_constant(df["bmi"])
y = df["diabetes"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["bmi"]], y)

df["pred_prob"] = clf.predict_proba(df[["bmi"]])[:,1]
df["pred_class"] = clf.predict(df[["bmi"]])

plt.scatter(df["bmi"], y)
plt.plot(df["bmi"], df["pred_prob"])
plt.title("BMI vs Diabetes")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()

















# **7 Temperature vs Failure**

df = pd.DataFrame({
  "temp": [50,55,60,65,70,75,80,85,90,95],
  "failure": [0,0,0,0,1,0,1,1,1,1]
})

X = sm.add_constant(df["temp"])
y = df["failure"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["temp"]], y)

df["pred_prob"] = clf.predict_proba(df[["temp"]])[:,1]
df["pred_class"] = clf.predict(df[["temp"]])

plt.scatter(df["temp"], y)
plt.plot(df["temp"], df["pred_prob"])
plt.title("Temperature vs Failure")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()






# **8 Pressure vs Defect**


df = pd.DataFrame({
  "pressure": [10,15,20,25,30,35,40,45,50,55],
  "defect": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["pressure"])
y = df["defect"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["pressure"]], y)

df["pred_prob"] = clf.predict_proba(df[["pressure"]])[:,1]
df["pred_class"] = clf.predict(df[["pressure"]])

plt.scatter(df["pressure"], y)
plt.plot(df["pressure"], df["pred_prob"])
plt.title("Pressure vs Defect")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()











# **9 Income vs Loan**

df = pd.DataFrame({
  "income": [20,25,30,35,40,45,50,55,60,65],
  "loan": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["income"])
y = df["loan"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["income"]], y)

df["pred_prob"] = clf.predict_proba(df[["income"]])[:,1]
df["pred_class"] = clf.predict(df[["income"]])

plt.scatter(df["income"], y)
plt.plot(df["income"], df["pred_prob"])
plt.title("Income vs Loan")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()








# ** 10 Credit Score vs Default**
df = pd.DataFrame({
  "score": [300,350,400,450,500,550,600,650,700,750],
  "default": [1,1,1,1,0,1,0,0,0,0]
})

X = sm.add_constant(df["score"])
y = df["default"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["score"]], y)

df["pred_prob"] = clf.predict_proba(df[["score"]])[:,1]
df["pred_class"] = clf.predict(df[["score"]])

plt.scatter(df["score"], y)
plt.plot(df["score"], df["pred_prob"])
plt.title("Score vs Default")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()












# **11 GPA vs Admission**


df = pd.DataFrame({
  "gpa": [2.0,2.2,2.5,2.7,3.0,3.2,3.5,3.7,3.8,4.0],
  "admit": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["gpa"])
y = df["admit"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["gpa"]], y)

df["pred_prob"] = clf.predict_proba(df[["gpa"]])[:,1]
df["pred_class"] = clf.predict(df[["gpa"]])

plt.scatter(df["gpa"], y)
plt.plot(df["gpa"], df["pred_prob"])
plt.title("GPA vs Admission")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()
























# **1 2 Visits vs Purchase**
df = pd.DataFrame({
  "visits": [1,2,3,4,5,6,7,8,9,10],
  "buy": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["visits"])
y = df["buy"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["visits"]], y)

df["pred_prob"] = clf.predict_proba(df[["visits"]])[:,1]
df["pred_class"] = clf.predict(df[["visits"]])

plt.scatter(df["visits"], y)
plt.plot(df["visits"], df["pred_prob"])
plt.title("Visits vs Purchase")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()























# ** 1 3 Speed vs Accident**
df = pd.DataFrame({
  "speed": [30,40,50,60,70,80,90,100,110,120],
  "accident": [0,0,0,0,1,0,1,1,1,1]
})

X = sm.add_constant(df["speed"])
y = df["accident"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["speed"]], y)

df["pred_prob"] = clf.predict_proba(df[["speed"]])[:,1]
df["pred_class"] = clf.predict(df[["speed"]])

plt.scatter(df["speed"], y)
plt.plot(df["speed"], df["pred_prob"])
plt.title("Speed vs Accident")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()























# ** 14 Attempts vs Breach**
df = pd.DataFrame({
  "attempts": [1,2,3,4,5,6,7,8,9,10],
  "breach": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["attempts"])
y = df["breach"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["attempts"]], y)

df["pred_prob"] = clf.predict_proba(df[["attempts"]])[:,1]
df["pred_class"] = clf.predict(df[["attempts"]])

plt.scatter(df["attempts"], y)
plt.plot(df["attempts"], df["pred_prob"])
plt.title("Attempts vs Breach")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()























# **15 Exercise vs Weight Loss**
df = pd.DataFrame({
  "hours": [1,2,3,4,5,6,7,8,9,10],
  "loss": [0,0,0,1,0,1,1,1,1,1]
})

X = sm.add_constant(df["hours"])
y = df["loss"]

model = sm.Logit(y, X).fit()
print(model.summary())

print("\nOdds Ratio:\n", np.exp(model.params))

clf = LogisticRegression()
clf.fit(df[["hours"]], y)

df["pred_prob"] = clf.predict_proba(df[["hours"]])[:,1]
df["pred_class"] = clf.predict(df[["hours"]])

plt.scatter(df["hours"], y)
plt.plot(df["hours"], df["pred_prob"])
plt.title("Exercise vs Weight Loss")
plt.show()

print("Accuracy:", accuracy_score(y, df["pred_class"]))
print(confusion_matrix(y, df["pred_class"]))

fpr, tpr, _ = roc_curve(y, df["pred_prob"])
plt.plot(fpr, tpr)
plt.show()