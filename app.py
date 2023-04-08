import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("model.pkl", "rb"))
dt = pickle.load(open("dictionary_map.pkl", "rb"))

st.header("Laptop Price Predictor!!!")

val1 = st.selectbox(
    'Company Name',
    (dt["company_name"].keys()))

val2 = st.selectbox(
    'Processor Name',
    (dt["processor_name"].keys()))

val3 = st.selectbox(
    'Processor Generation',
    (dt["processor_generation"].keys()))

val4 = st.selectbox(
    'Operating System',
    ("DOS ","64 bit Windows 11 ", "64 bit Windows 10 ", "Windows 11 ", "Mac OS ", "Windows 10 ", "Chrome "))

val5 = st.selectbox(
    'Storage (SSD)',
    (128, 256, 512))

val6 = st.selectbox(
    'Screen Size',
    (14, 15.6, 16, 17))

val7 = st.selectbox(
    'Ram Capacity (GB)',
    (4, 8, 16, 32))

val8 = st.selectbox(
    'Ram Type',
    (dt["ram_type"].keys()))

value = [dt["company_name"][val1], dt["processor_name"][val2], dt["processor_generation"][val3],
dt["operating_system"][val4], int(val5), int(val6), int(val7), dt["ram_type"][val8]]

price = model.predict([value])
print(price)
st.write('\n\tPrice of the laptop approxmately ₹', np.round(price[0], decimals=2))