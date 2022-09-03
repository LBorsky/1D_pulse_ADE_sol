# function

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
st.title("1-D ADE solution, IC=pulse")

"""
def conc(x,t=1,Q=5,D=0.001,x_0=0,U=1,sig=3):
    return Q / (4 * np.pi * D * t) ** 0.5 * np.exp(-((x - x_0 - U * t) ** 2) / (2 * sig ** 2))
    
xlist = np.linspace(0,100,num=1000)

# streamlit

st.title("1-D ADE solution, IC=pulse")
t = st.slider("Time of sampling [s]", 0.1, 50.1, 5)
ylist = conc(x=xlist,t=t)
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(xlist, ylist)
ax.set_xlabel('$t$ (sec)')
ax.set_ylabel('$C$ (mg/L)')
st.pyplot(fig)
"""
