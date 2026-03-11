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



# -------------| Multiple problems |-------------




df9 = pd.DataFrame({
  "id" : [1,2,2,3,np.nan],
  "age" : [20,25,25,-10,30],
  "income" : ["10000","20000","20000","not available","30000"]
})


df9_clean = df9.copy()
df9_clean["id"] = df9_clean["id"].replace(np.nan,0)
df9_clean["age"] = np.where(df9_clean["age"]<0,df9_clean["age"].mean(),df9_clean["age"])
df9_clean["income"] = df9_clean["income"].replace("not available",np.nan)
df9_clean["income"] = pd.to_numeric(df9_clean["income"])
df9_clean["income"] = df9_clean["income"].replace(np.nan,df9_clean["income"].mean())
df9_clean = df9_clean.drop_duplicates()


# -------------| Advanced Problems |-------------

import pandas as pd
import numpy as np

df10 = pd.DataFrame({
  "year" : ["2020","2021","2021","2022"],
  "sales_q1" : ["100","150","150","200"],
  "sales_q2" : ["120",np.nan,"170","210"]
})



df10_clean = df10.copy()
df10_clean["sales_q1"] = pd.to_numeric(df10_clean["sales_q1"])
df10_clean["sales_q2"] = pd.to_numeric(df10_clean["sales_q2"])
df10_clean["sales_q2"] = df10_clean["sales_q2"].replace(np.nan,df10_clean["sales_q2"].median())
df10_clean["total_sales"] = df10_clean["sales_q1"] + df10_clean["sales_q2"]



# -------------| Complex DataSet |-------------


df11 = pd.DataFrame({
  "id" : [1,2,2,np.nan,4,5],
  "gender" : ["M","F","F","Unknown","M",np.nan],
  "age" : ["15","thirty","30","40",np.nan,"50"],
  "income" : ["50000","60000","60000","Unknown","70000","80000"]
})


df11_clean = df11.copy()
df11_clean["id"] = df11_clean["id"].replace(np.nan,0)
df11_clean["income"] = df11_clean["income"].replace("Unknown",np.nan)
df11_clean["income"] = pd.to_numeric(df11_clean["income"])
df11_clean["income"] = df11_clean["income"].replace(np.nan,df11_clean["income"].mean())
df11_clean["gender"] = df11_clean["gender"].replace("Unknown",np.nan)
df11_clean["gender"] = df11_clean["gender"].fillna("Other")
