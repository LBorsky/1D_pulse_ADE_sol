# function
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def conc(x,T=1,Q=5,D=0.005,X_0=0,U=1,S=3):
    return Q / (4 * np.pi * D * T) ** 0.5 * np.exp(-((x - X_0 - U * T) ** 2) / (2 * S ** 2))
    
xlist = np.linspace(0,100,num=1000)

# streamlit
st.title("1-D ADE solution, IC=pulse")
t = st.slider("Time of sampling [sec]", 1, 50, 5)
q = st.slider("Initial mass/area of contaminant [kg/m^2]", 1, 10, 5)
u = st.slider("Velocity of fluid [m/sec]", 0, 5, 2)
x_0 = st.slider("Location of contemination [m]", 0, 40, 0)
d = st.selectbox("Diffusion coefficient [m^2/s], (0.00001, 0.0001, 0.001))
ylist = conc(x=xlist,T=t,Q=q,D=d,X_0=x_0,U=u)
fig, ax = plt.subplots(figsize=(6,6))
plt.axis([0,100,0,50])
ax.plot(xlist, ylist, color="blue", linewidth=2)
ax.set_xlabel('$x  [m]$')
ax.set_ylabel('$C  [kg/m^3]$')
st.pyplot(fig)

