import pandas as pd
import numpy as np

df1 = pd.DataFrame({
  'id': [1, 2, 3, np.nan, 5],
  'age': [25, np.nan, 35, 40, np.nan],
  'income': [50000, 60000, np.nan, 80000, 90000]
})


# -------------| Removing missing values |-------------


# 1. Removing columns with missing values

df1_copy = df1.dropna()

# 2. Replacing with mean

df1_age = df1.copy()
df1_age["age"] = df1_age["age"].fillna(df1_age["age"].mean())


# 3. Replacing with zero

df1_income = df1.copy()
df1_income["income"] = df1_income["income"].fillna(0)





# -------------| Convert Types |-------------



df2 = pd.DataFrame({
  "student" : ["A","B","C","D"],
  "score" : ["90","85","88","92"],
  "passed": ["yes","yes","no","yes"]
})



df2.info()
df_num.info()
df2.describe()



df_num = df2.copy()
df_num["score"] = pd.to_numeric(df_num["score"])
df_num["passed"] = df_num["passed"].astype("category")



# -------------| Duplicates |-------------


df3 = pd.DataFrame({
  'product' : ["A","B","A","C","C"],
  "price" : [10,20,10,15,15]
})


df3_all = df3.drop_duplicates()
df3_prod = df3.drop_duplicates(subset=["product"],keep="first")



# -------------| Rename |-------------

df4 = pd.DataFrame({
  "x1":[10,20,30],
  "x2":[5,6,7]
})


df4_rename = df4.rename(columns={"x1":"height","x2":"weight"})



# -------------| Filter Invalid |-------------


df5 = pd.DataFrame({
  "person" : ["john","anna","mike","sara"],
  "age" : [22,-5,200,30]
})


df_filter = df5[(df5["age"] > 0) & (df5["age"] < 100)]




# -------------| New Variables |-------------


df6 = pd.DataFrame({
  'name': ["A", "B", "C"],
  'math': [80, 90, 70],
  'science': [85, 88, 78]
})

df6_new = df6.copy()
df6_new["total"] = df6_new["math"]+df6_new["science"]
df6_new["avg"] = df6_new["total"]/2



