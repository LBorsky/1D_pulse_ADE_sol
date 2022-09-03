# function

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def conc(x,T=1,Q=5,D=0.005,x_0=0,U=1,sig=3):
    return Q / (4 * np.pi * D * t) ** 0.5 * np.exp(-((x - x_0 - U * t) ** 2) / (2 * sig ** 2))
    
xlist = np.linspace(0,100,num=1000)

# streamlit
st.title("1-D ADE solution, IC=pulse")
t = st.slider("Time of sampling [sec]", 1, 50, 5)
u = st.slider("Velocity of fluid [m/sec]", 0.1, 5, 1)
ylist = conc(x=xlist,T=t,U=u)
fig, ax = plt.subplots(figsize=(6,6))
plt.axis([0,50,0,50])
ax.plot(xlist, ylist, color="blue", linewidth=2)
ax.set_xlabel('$x$ [m]')
ax.set_ylabel('$C$ (mg/L)')
st.pyplot(fig)

