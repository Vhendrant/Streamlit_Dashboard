import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

place_name = ["Aotizhongxin", "Changping", "Dingling", "Dongsi", "Guanyuan", "Gucheng", "Huairou", "Nongzhangguan",
              "Shunyi", "Tiantan", "Wanliu", "Wanshouxigong"]

st.header("Yearly PM10 and CO Levels in China")
PM10_select_data = st.selectbox("Select Data to display: ", place_name, key="pm10 data")
data_selected = pd.read_csv("Yearly_PM10_Levels_Updated_" + PM10_select_data + ".csv")
st.subheader("Yearly PM10 Levels in " + PM10_select_data)

PM10_fig, PM10_ax = plt.subplots(figsize=(16, 8))
PM10_ax.plot(
    data_selected["year"], data_selected["PM10"],
    marker="o", linewidth="3.5", color="#90CAF9"
)
PM10_ax.tick_params(axis='y', labelsize=20)
PM10_ax.tick_params(axis='x', labelsize=20)

st.pyplot(PM10_fig)


CO_select_data = st.selectbox("Select Data to display: ", place_name, key="CO data")
data_selected = pd.read_csv("Yearly_CO_Levels_Updated_" + CO_select_data + ".csv")
st.subheader("Yearly CO Levels in " + CO_select_data)
CO_fig, CO_ax = plt.subplots(figsize=(16, 8))
CO_ax.plot(
    data_selected["year"], data_selected["CO"],
    marker="o", linewidth="3.5", color="#90CAF9"
)
CO_ax.tick_params(axis='y', labelsize=20)
CO_ax.tick_params(axis='x', labelsize=20)

st.pyplot(CO_fig)
