import pandas as pd 
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv("G:\\Courses\\NAVVTAC\\2nd Month\\Practice\\Marketing data\\Marketing_Data.csv")



# -------------------------------------
#       Training Model
# -------------------------------------



y = data[["sales"]]
X = data[["youtube" , "facebook" , "newspaper"]]

model = LinearRegression()
model.fit(X,y)

coef = model.coef_
intercept = model.intercept_


test_df = pd.DataFrame({
    "youtube": [0.84, 500, 100],
    "facebook": [0, 50, 10],
    "newspaper": [0.36, 40, 5]
})
predicted_sales = model.predict(test_df)
print(predicted_sales[0][0])




# -------------------------------------
#       Streamlit webpage
# -------------------------------------

st.set_page_config(page_title="Sales Predictor", page_icon="📊", layout="wide")

st.title("📊 Sales Predictor App")
st.write("Adjust the marketing budget using the sliders and predict sales instantly.")

# Sidebar
st.sidebar.header("🎯 Define Your Budget")

youtube = st.sidebar.slider(
    "📺 YouTube Budget",
    float(data.youtube.min()),
    float(data.youtube.max()),
    float(data.youtube.mean()),
)

facebook = st.sidebar.slider(
    "📘 Facebook Budget",
    float(data.facebook.min()),
    float(data.facebook.max()),
    float(data.facebook.mean()),
)

newspaper = st.sidebar.slider(
    "📰 Newspaper Budget",
    float(data.newspaper.min()),
    float(data.newspaper.max()),
    float(data.newspaper.mean()),
)

# Input array
input_arr = [[youtube, facebook, newspaper]]

# Prediction
predicted_sales = round(model.predict(input_arr)[0][0])

# ---------------- UI OUTPUT ----------------

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric("📺 YouTube", f"$ {round(youtube, 2)}")
col2.metric("📘 Facebook", f"$ {round(facebook, 2)}")
col3.metric("📰 Newspaper", f"$ {round(newspaper, 2)}")

st.markdown("---")

st.subheader("📈 Predicted Sales")

st.success(f"💰 Expected Sales: {predicted_sales} units")

# Optional explanation
st.info("This prediction is based on a Linear Regression model trained on marketing spend data.")

st.subheader("📊 Model Parameters")

coef_df = pd.DataFrame({
    "Feature": ["YouTube", "Facebook", "Newspaper"],
    "Coefficient": [coef[0][0], coef[0][1], coef[0][2]]
})

st.write("### Coefficients")
st.dataframe(coef_df)

st.write("### Intercept")
st.write(f"💡 Intercept: {intercept[0]:.4f}")




# Footer
st.markdown("---")
st.caption("Built by Ammar using Streamlit")
