import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load df and pipeline separately, don't overwrite df with pipe
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title("Laptop Price Predictor App")

company = st.selectbox("Manufacturing Company", df['Company'].unique(), index=5)
typename = st.radio("Type Name", df['TypeName'].unique(), index=1)
cpu = st.selectbox("Processor", df['Cpu'].unique(), index=0)
ram = st.radio("RAM (in GB)", [4, 8, 12, 16, 32, 64, 128], index=1, horizontal=True)
gpu = st.selectbox("Graphics Card", df['Gpu'].unique(), index=1)
os = st.selectbox("Operating System", df['OpSys'].unique(), index=2)  # Added parentheses after unique()
weight = st.slider("Weight (in kg)", min_value=0.7, max_value=4.8, value=2.5, step=0.1)
touchscreen = st.selectbox("Touchscreen", ['Yes', 'No'], index=1)
ips = st.selectbox("IPS Display?", ['Yes', 'No'], index=1)
cpu_speed = st.slider("CPU Speed (in GHz)", min_value=0.9, max_value=4.0, value=2.5, step=0.1)
screen_size = st.slider("Screen Size (in inches, Measured diagonally)", min_value=10.0, max_value=18.5, value=15.6, step=0.1)
screen_resolution = st.selectbox("Screen Resolutions", ["1366x768", "1920x1080", "1600x900", "2560x1440", "3200x1800", "3840x2160", "2880x1800", "2560x1600", "1440x900", "1024x600", "1280x800"],index=1)

if st.button("PREDICT PRESS"):
    ppi = None
    if (ips=='Yes'):
        ips=1
    else:
        ips=0
    if(touchscreen=='Yes'):
          touchscreen=1
    else:
        touchscreen=0
    X_res=int(screen_resolution.spilt('x')[0])
    Y_res=int(screen_resolution.split('x')[1])
    ppi = ((X_res**2)+(Y_res**2))**0.5/screen_size

    query=np.array([[company,typename,cpu,ram,gpu,os,weight,ips,touchscreen,cpu_speed,ppi]])
    op=pipe.predict(query)
    f_op=int(round(op[0],-2))
    st.subheader("the estimated price of laptop with thw above selescted configuration is ₹ "+str(f_op))
